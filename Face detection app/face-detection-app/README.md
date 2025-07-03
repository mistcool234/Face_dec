# Face Detection Application

This project is a face detection application that utilizes a camera to capture video frames and detect faces in real-time. It is built using Python and leverages OpenCV for image processing.

## Project Structure

```
face-detection-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── camera.py        # Handles camera initialization and frame capture
│   ├── face_detector.py  # Contains the face detection logic
│   └── utils.py         # Utility functions for drawing and displaying frames
├── requirements.txt      # Lists the project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd face-detection-app
   ```

2. **Install the required dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the camera, start capturing video frames, and process them for face detection. Detected faces will be highlighted in the video feed.

## Dependencies

- `opencv-python`: For image processing and computer vision tasks.
- `numpy`: For numerical operations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.