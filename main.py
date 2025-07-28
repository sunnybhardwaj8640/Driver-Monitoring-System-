import cv2
import time
from distraction_detector import DistractionDetector
from report_generator import generate_report

cap = cv2.VideoCapture(0)
detector = DistractionDetector()
distraction_count = 0
start_time = time.time()

print("[INFO] Starting Driver Monitoring System. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, distracted = detector.process_frame(frame)
    if distracted:
        distraction_count += 1

    cv2.imshow("Driver Monitoring System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

duration = int(time.time() - start_time)
cap.release()
cv2.destroyAllWindows()

generate_report(distraction_count, duration)
print(f"[INFO] Monitoring session ended. Report generated.")
