FROM python:3.11-slim

# OpenCV runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libgl1-mesa-glx \
      libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-download YOLO model weights so first request is instant
RUN python -c "from ultralytics import YOLO; YOLO('yolo11n-pose.pt')"

EXPOSE 5000

CMD ["python", "app.py"]
