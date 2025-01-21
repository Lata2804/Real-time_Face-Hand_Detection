import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start the camera
print("To start the camera, type 'start' and press enter:")
while True:
    user_input = input()
    if user_input.lower() == 'start':
        break
    else:
        print("Invalid input. Please type 'start' to begin.")

cap = cv2.VideoCapture(0)  # Use 0 for default camera

# Check if the camera opened successfully or not
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.6) as face_detection, \
     mp_hands.Hands(min_detection_confidence=0.5, max_num_hands=10, min_tracking_confidence=0.5) as hands:
    while True:
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_face = face_detection.process(image)
        results_hands = hands.process(image)

        # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results_face.detections:
            for detection in results_face.detections:
                mp_drawing.draw_detection(image, detection)
        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2),
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2))

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Demo', cv2.flip(image, 1))

        # Press 'a' to exit
        if cv2.waitKey(5) & 0xFF == ord('a'):
            break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
