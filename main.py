from src.detector import PoseDetector
from src.vision import VideoStream
import time

def main():
    # Initialize components
    detector = PoseDetector(model_name='yolo11n-pose.pt')
    stream = VideoStream(source=0)
    
    print("Initializing...")
    print("Raise both hands above your head to trigger an alert!")
    
    # Run the stream
    results = detector.detect_pose(source=0, show=True, imgsz=640)
    
    try:
        for result in results:
            # Check for specific pose logic
            if detector.check_hands_raised(result):
                print("ALERT: Hands Raised Detected!")
            
            # Simple FPS tracking in terminal
            fps = stream.get_fps()
            
    except KeyboardInterrupt:
        print("\n Exiting")
    finally:
        stream.release()

if __name__ == "__main__":
    main()
