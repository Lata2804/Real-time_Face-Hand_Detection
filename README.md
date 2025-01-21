# Real-Time Face and Hand Detection using MediaPipe

This project demonstrates real-time detection of faces and hands using MediaPipe and OpenCV in Python. The application processes live video feed from a webcam to detect faces and hands, and overlays annotations on the video stream.

## Features
- Real-time face detection with bounding boxes and key points.
- Real-time hand detection with landmarks and connections.
- Simple interface for starting the camera and stopping with a key press.

## Demo


*video of the app in action.*

## Technologies Used
- Python: Programming language for the application.
- OpenCV: For accessing the webcam and processing images.
- MediaPipe: For efficient and accurate face and hand detection.
- Hardware Requirement: Webcam (default or external).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Lata2804/Real-time_Face-Hand_Detection.git
   cd Real-time_Face-Hand_Detection
   ```

2. Install the required dependencies:
   ```bash
   pip install mediapipe
   pip install python
   ```

3. Run the script:
   ```bash
   python Face&Hand_Detection.py
   ```

## Usage
1. When prompted, type `start` and press enter to initiate the camera feed.
2. The webcam feed will appear, showing detected faces and hands with annotations.
3. Press the `a` key to stop the program and close the webcam feed.

## Limitations
- The accuracy of detection depends on the lighting and quality of the webcam.
- Detection may not perform well with very low resolution or obscured faces/hands.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
