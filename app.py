import base64
import sys
import os

import cv2
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from detector import PoseDetector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pose-analytics-secret'
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')

detector = PoseDetector(model_name='yolo11n-pose.pt')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('frame')
def handle_frame(data: str) -> None:
    # Strip the data URL prefix
    if ',' in data:
        data = data.split(',', 1)[1]

    img_bytes = base64.b64decode(data)
    arr = np.frombuffer(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if frame is None:
        return

    results = detector.model(frame, verbose=False)

    hands_raised = False
    annotated = frame

    if results:
        result = results[0]
        annotated = result.plot()
        hands_raised = detector.check_hands_raised(result)

    _, buffer = cv2.imencode('.jpg', annotated, [cv2.IMWRITE_JPEG_QUALITY, 75])
    encoded = base64.b64encode(buffer).decode('utf-8')

    socketio.emit('response', {
        'image': 'data:image/jpeg;base64,' + encoded,
        'hands_raised': hands_raised,
    })


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
