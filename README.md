# SignSense - Sign Language Interpreter

## Team Information
- **Team Name**: Team Coconut  
- **Team Number**: 10  
- **Team Members**: Dhruv Charan, Ryland Hill, Abdullah Liaqat Ali, Shaan Nair, Taha Shahid, Zayd Syed  
- **Git Repository**: [SignSense Repository](https://git.uwaterloo.ca/r5hill/se101_project)

---

## Project Overview

**SignSense** is an innovative system designed to bridge communication gaps by interpreting sign language and spoken language. By combining hardware and software components, SignSense allows seamless interaction between users, making communication accessible for everyone.

### Key Features

1. **Capture Gestures**:
   - The camera recognizes hand gestures and detects facial expressions to translate them into text.

2. **Convert Gestures to Text**:
   - Recognized gestures are processed and displayed as text in real-time.

3. **Speech Recognition**:
   - Converts spoken words captured by the microphone into text.

4. **Text-to-Speech Conversion**:
   - Converts displayed text into spoken language for dynamic interactions.

---

## Technical Implementation

1. **Setup**:
   - The Raspberry Pi Zero 2W runs a Python script on boot, starting a Flask server and capturing video feed using OpenCV and Picamera2.
   - This video feed is accessible on the LAN network via the Flask server.

2. **Processing**:
   - The external computer analyzes the video feed with Mediapipe and TensorFlow to interpret gestures and letters.
   - Sentences are detected and corrected for grammar/spelling issues using `pyttsx3` and `nltk`.

3. **Output**:
   - Text is converted into speech using `espeak` and sent back to the Raspberry Pi for playback via headphones.

### Challenges

- Limited processing power of the Raspberry Pi Zero 2W necessitated offloading tasks to an external computer.
- Delays in integrating features like facial expression recognition and screen display due to hardware limitations.

---

## Professional Considerations

### Privacy & Safety
- Live video feed raises potential privacy concerns.
- Wireless network vulnerabilities could expose the video feed to interception.

### Intellectual Property
The following libraries and tools were used under permissible licenses:
1. OpenCV (Apache 2.0)
2. Mediapipe (Apache 2.0)
3. TensorFlow (Apache 2.0)
4. NLTK (Apache 2.0)
5. Flask (BSD 3-Clause)
6. Picamera2 (BSD 2-Clause)
7. NumPy (BSD License)
8. LanguageToolPython (LGPL 2.1)

---

## Project Outcome
Despite hardware limitations, the core functionality of interpreting gestures and converting them into text was successfully implemented. The project provided valuable insights into hardware constraints and emphasized the importance of thorough research and planning.

### Budget Analysis
- **Labor**: 96 hours x $25/hour = $2,400  
- **Hardware**: $73  
- **Total**: $2,473  

---

## User Manual

### Getting Started

1. **Hardware Setup**:
   - Connect the Raspberry Pi to a camera module and headphones.
   - Ensure both the Raspberry Pi and external computer are on the same LAN.

2. **Software Requirements**:
   - Install the required Python libraries: OpenCV, Mediapipe, TensorFlow, Flask, Pyttsx3, NLTK.
   - Start the Flask server on the Raspberry Pi.

3. **Using SignSense**:
   - Perform hand gestures in front of the camera.
   - View the interpreted text on the external computer.
   - Listen to the text-to-speech output via headphones.

### Troubleshooting
- Ensure the camera and microphone are connected properly.
- Verify the Flask server is running and accessible.
- Check for any missing Python dependencies.

---

## Roadmap

Future improvements include:
1. Integrating facial expression recognition.
2. Adding a display screen for real-time feedback.
3. Optimizing processing to eliminate reliance on external computers.

---

## Contribution Guidelines

1. Fork the repository and create a new branch.
2. Submit pull requests with clear descriptions of changes.
3. Use test cases provided in `updated_main.py` to validate contributions.

---

## Authors
- Dhruv Charan
- Ryland Hill
- Abdullah Liaqat Ali
- Shaan Nair
- Taha Shahid
- Zayd Syed

---

## License
This project uses libraries under open-source licenses (Apache 2.0, BSD, LGPL 2.1). Refer to individual library documentation for details.

---

## Project Status
Active development has concluded. Contributions are welcome to enhance functionality and add features.
