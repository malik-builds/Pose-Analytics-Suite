import time
import cv2

class VideoStream:
    
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        self.prev_time = 0
        self.fps = 0

    def get_fps(self):
        curr_time = time.time()
        fps = 1 / (curr_time - self.prev_time)
        self.prev_time = curr_time
        return int(fps)

    def release(self):
        self.cap.release()
