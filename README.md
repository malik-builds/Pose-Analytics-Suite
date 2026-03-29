# Pose Analytics Suite 

A professional, real-time computer vision application that monitors human poses and triggers actions based on specific movements. Powered by SOTA **YOLOv11-Pose** and optimized for edge performance.

## Features
- **Real-Time Pose Estimation:** Tracks 17 human keypoints at 30+ FPS.
- **Action Logic:** Automated detection for specific poses (e.g., "Hands Raised" alert).
- **Pro Performance:** Optimized stream handling with rolling FPS monitoring.
- **Modular Design:** Built with a production-ready repository structure.

## Tech Stack
- **Python 3.10+**
- **Ultralytics YOLOv11** (Pose Model)
- **OpenCV** (Vision processing)
- **PyTorch** (Inference engine)
- **Flask + Flask-SocketIO** (Web UI / real-time streaming)

## Repository Structure
```text
Pose-Analytics-Suite/
├── src/
│   ├── detector.py      # AI Logic & Pose Analytics
│   └── vision.py        # Stream Handling & FPS Utilities
├── templates/
│   └── index.html       # Web UI (webcam + live feed)
├── app.py               # Flask + SocketIO Web Server
├── main.py              # CLI Entry Point
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container image
├── docker-compose.yml   # Compose service
└── .gitignore
```

## Quick Start

### CLI (local webcam + OpenCV window)

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run:**
   ```bash
   python main.py
   ```

3. **Try the Demo:**
   Raise both hands above your head while in front of the camera to trigger the **Terminal Alert**.

### Web UI (browser webcam + real-time feed)

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```

3. **Open** `http://localhost:5000` in your browser and allow camera access.
   The annotated feed and live "Hands Raised: YES / NO" status will appear.

### Docker

```bash
docker compose up --build
```

Then open `http://localhost:5000`.

> **Note:** The Docker build pre-downloads the YOLO model (~6MB), so the first request is instant. Expect a ~2-3GB image due to PyTorch.

## 📄 License & Attribution
- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics).
- Model: `yolo26n-pose.pt`
