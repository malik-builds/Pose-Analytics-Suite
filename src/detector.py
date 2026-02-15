from ultralytics import YOLO

class PoseDetector:
    def __init__(self, model_name='yolo11n-pose.pt'):
        self.model = YOLO(model_name)
    def detect_pose(self, source=0, show=True, imgsz=640):
        return self.model(source=source, show=show, stream=True, imgsz=imgsz)

    def check_hands_raised(self, result):
        """
        Determines if any detected person has both hands raised above their shoulders.
        
        In image coordinates, the Y-axis starts at 0 at the top and increases downwards.
        Therefore, a 'raised' hand is one where the wrist's Y-coordinate is smaller 
        than the shoulder's Y-coordinate.
        """
        LEFT_SHOULDER_INDEX, RIGHT_SHOULDER_INDEX = 5, 6 # these were extracted from the COCO Keypoint map
        LEFT_WRIST_INDEX, RIGHT_WRIST_INDEX = 9, 10

        if result.keypoints is None or len(result.keypoints.xy) == 0:
            return False

        for person_points in result.keypoints.xy:
            if person_points.shape[0] < 11:
                continue

            left_shoulder_y = person_points[LEFT_SHOULDER_INDEX][1]
            right_shoulder_y = person_points[RIGHT_SHOULDER_INDEX][1]
            left_wrist_y = person_points[LEFT_WRIST_INDEX][1]
            right_wrist_y = person_points[RIGHT_WRIST_INDEX][1]

            left_hand_raised = left_wrist_y < left_shoulder_y
            right_hand_raised = right_wrist_y < right_shoulder_y

            if left_hand_raised and right_hand_raised:
                return True

        return False

