import cv2
import mediapipe as mp
import pygame

class DistractionDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)
        self.distracted = False
        pygame.mixer.init()
        self.alarm = pygame.mixer.Sound("assets/alarm.wav")

    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)
        if not results.multi_face_landmarks:
            self.distracted = True
            self.alarm.play()
            cv2.putText(frame, "DISTRACTED!", (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
            return frame, True
        else:
            self.distracted = False
            self.alarm.stop()
            cv2.putText(frame, "Focused", (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)
            return frame, False
