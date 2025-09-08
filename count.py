import cv2
import dlib
import threading
import time

# Configuration parameters
FRAME_SCALE = 0.5         # Resize frame to 50% for faster processing
FPS_LIMIT = 10            # Process at 10 FPS max
UPDATE_INTERVAL = 3       # Update face count every 3 seconds

# Initialize detector and webcam
detector = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture(0)

# Shared frame variable with threading lock
shared_frame = None
lock = threading.Lock()

# Variables for timed updates
last_update_time = time.time()
last_face_count = 0

def capture_frames():
    """Capture frames continuously in a separate thread."""
    global shared_frame
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        with lock:
            shared_frame = frame

# Start capture thread
threading.Thread(target=capture_frames, daemon=True).start()

def process_frame(frame):
    """Detect faces and annotate the frame."""
    global last_update_time, last_face_count

    resized = cv2.resize(frame, (0, 0), fx=FRAME_SCALE, fy=FRAME_SCALE)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Update face count every 3 seconds
    current_time = time.time()
    if current_time - last_update_time >= UPDATE_INTERVAL:
        last_face_count = len(faces)
        last_update_time = current_time
        print(f"Updated Face Count: {last_face_count}")  # Print to console

    # Draw bounding boxes
    scale_back = lambda x: int(x / FRAME_SCALE)
    for i, face in enumerate(faces):
        x, y = scale_back(face.left()), scale_back(face.top())
        x1, y1 = scale_back(face.right()), scale_back(face.bottom())
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        cv2.putText(frame, f'Face {i+1}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Show the *last updated* face count on frame
    cv2.putText(frame, f'Total Faces: {last_face_count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    return frame

# Main loop with FPS control
prev_time = 0
while True:
    current_time = time.time()
    if current_time - prev_time >= 1 / FPS_LIMIT:
        prev_time = current_time
        with lock:
            if shared_frame is not None:
                output = process_frame(shared_frame.copy())
                cv2.imshow('Optimized Face Counter (3s Updates)', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
