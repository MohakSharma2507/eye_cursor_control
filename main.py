import cv2
import mediapipe as mp
import pyautogui

# Accessing the camera
cam = cv2.VideoCapture(0)

# Initialize Face Mesh from MediaPipe
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()  # Get screen size

while True:
    # Capture the frame from the camera
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror-like effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark
        frame_h, frame_w, _ = frame.shape

        # Using landmark 475 to move the mouse
        for id, landmark in enumerate(landmarks[474:478]):  # Eye-related landmarks
            x = int(landmark.x * frame_w)  # Get x coordinate on the frame
            y = int(landmark.y * frame_h)  # Get y coordinate on the frame
            cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Visual feedback with a small circle

            # Use landmark 475 for controlling the cursor
            if id == 1:
                # Map the frame coordinates to screen size
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)

                print(f"Moving cursor to Screen X: {screen_x}, Screen Y: {screen_y}")
                pyautogui.moveTo(screen_x, screen_y)  # Move the cursor directly to the mapped coordinates

        # Optional: Left-eye blink detection for clicking
        left = [landmarks[145], landmarks[159]]  # Eyelid landmarks for blink detection
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Yellow circles for blink detection landmarks

        # Blink detection logic (if the distance between eyelids is small)
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    # Display the video feed with the face mesh overlay
    cv2.imshow("Eye Control Mouse", frame)

    # Exit loop when 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # ASCII for Esc key is 27
        break

# Release the camera and close windows
cam.release()
cv2.destroyAllWindows()
