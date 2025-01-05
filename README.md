# SignSense - Sign Language Interpreter

## Overview

**Software Engineering 1A Design Project @ University of Waterloo.** 

**Team Name:** Team Coconut
**Team Members:** Dhruv Charan, Ryland Hill, Abdullah Liaqat Ali, Shaan Nair, Taha Shahid, Zayd Syed  

**SignSense** is a system designed to bridge communication between individuals using sign language and those who do not understand it. The project integrates hardware and software to interpret gestures, speech, and text for seamless interaction.

---

## Features

- **Gesture Recognition:** Captures hand gestures using a camera and translates them into text.  
- **Speech Recognition:** Converts spoken language into text.  
- **Text-to-Speech Conversion:** Outputs text as spoken language for enhanced communication.  

### Current Implementation
- Converts gestures into text, played through headphones.
- External processing using Python, TensorFlow, Mediapipe, and Flask for gesture and language processing.

---

## Technical Details

1. **System Design**
   - Raspberry Pi Zero 2W for initial input processing.
   - Flask server for communication between Raspberry Pi and an external computer.
   - TensorFlow and Mediapipe for gesture recognition.

2. **Data Flow**
   - Video feed captured by the Raspberry Pi is analyzed externally for letter recognition.
   - Text output is checked for grammar/spelling using `nltk` and formatted into sentences.
   - Text is converted to speech on the Raspberry Pi using `espeak`.

---

## Setup Instructions

### Requirements
- Raspberry Pi Zero 2W
- Camera module
- External computer with Python 3.9+ and necessary libraries

### Steps
1. Clone the repository:
   ```bash
   git clone https://git.uwaterloo.ca/abdullahlali/sign-language-interpreter.git
   cd sign-language-interpreter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the Raspberry Pi:
   - Enable LAN connection and Flask server.
   - Configure the camera module.
4. Run the system:
   - On Raspberry Pi:
     ```bash
      python3 /home/pi/Desktop/flaskie/flaskie.py
     ```
   - On external computer:
     ```bash
     python process_video_feed.py
     ```

---

## How to Use

1. **Start the System**:
   - Ensure the Raspberry Pi and the external computer are connected to the same LAN.
   - Run the server on the Raspberry Pi and the processing script on the external computer as described in the setup instructions.

2. **Input Gestures**:
   - Use hand gestures in front of the camera module connected to the Raspberry Pi.
   - The system will recognize the gestures and convert them into corresponding text.

3. **View and Listen to Outputs**:
   - The recognized text will be processed and sent to the text-to-speech module.
   - The output will be played through the connected headphones.

4. **Speech-to-Text**:
   - Speak into the microphone connected to the system.
   - The system will convert the speech into text for further interaction.

---

## Challenges and Limitations

- **Processing Power:** Limited by Raspberry Pi Zero 2W, requiring external computation.  
- **Incomplete Features:** Facial expression recognition and display integration were not implemented due to time constraints.  

---

## Future Enhancements

- Use a more powerful microcontroller for onboard processing.  
- Add facial expression recognition for emotional context.  
- Integrate a display for real-time interaction feedback.  

---

## License and Dependencies

This project relies on several open-source libraries:
- **OpenCV, Mediapipe, TensorFlow** (Apache 2.0)  
- **Flask** (BSD 3-Clause)  
- **NLTK** (Apache 2.0)  
- **Picamera2** (BSD 2-Clause)  

All libraries are free for commercial use under their respective licenses.
