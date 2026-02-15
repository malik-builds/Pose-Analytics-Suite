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

## Repository Structure
```text
Object_Detection/
├── src/
│   ├── detector.py   # AI Logic & Pose Analytics
│   └── vision.py     # Stream Handling & FPS Utilities
├── main.py           # Application Entry Point
└── .gitignore        # Standards-compliant ignores
```

## Quick Start

1. **Install Dependencies:**
   ```bash
   pip install ultralytics opencv-python torch
   ```

2. **Run the Suite:**
   ```bash
   python main.py
   ```

3. **Try the Demo:**
   Raise both hands above your head while in front of the camera to trigger the **Terminal Alert**.

## 📄 License & Attribution
- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics).
- Model: `yolo26n-pose.pt`
