**Eye-Controlled Mouse Using Face Landmarks**

This project uses facial landmark detection via computer vision to control the mouse cursor using eye movements. The project leverages real-time video processing and facial mesh tracking to allow users to move their cursor by tracking their eye position, with blink detection for clicking.

**Project Features:**

Facial Landmark Detection: Utilizes MediaPipe’s FaceMesh module to detect and track specific landmarks around the eyes for real-time control.
Cursor Movement: Maps the movement of the user's eye to screen coordinates, allowing cursor movement without any physical input devices.
Blink Detection: Detects eye blinks by tracking the distance between eyelid landmarks. A blink triggers a mouse click using pyautogui.
Cross-Platform: Can be run on various platforms, tested on macOS (M3) and Windows.

**Technical Details:**

OpenCV: Captures video feed from the webcam and processes each frame to detect face and eye landmarks.
MediaPipe FaceMesh: Identifies facial landmarks in real time and provides accurate tracking of eye movements.
PyAutoGUI: Simulates mouse movement and clicking actions based on eye movement and blink detection.

**How it Works:**

The webcam captures the user's face in real-time.
FaceMesh detects landmarks on the user's face, focusing on the eyes.
Eye movements are mapped to screen coordinates, allowing the user to control the mouse cursor.
When a blink is detected, a mouse click is triggered.

**Technologies Used:**

Python
OpenCV
MediaPipe (FaceMesh)
PyAutoGUI
Future Enhancements:

Improve blink detection accuracy to reduce false clicks.
Add support for right-click and drag using different eye gestures.
Optimize performance for smoother cursor movement.
