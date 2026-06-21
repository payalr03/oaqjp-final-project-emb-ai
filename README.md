# Final project - NPL Emotion Detection

## Emotion Detection Web Application

A web application that analyzes the emotional content of text using IBM Watson NLP API.

## Features
- Detects emotions: anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion in the given text
- Handles blank/invalid input gracefully

## Technologies Used
- Python
- Flask
- IBM Watson NLP API
- HTML/CSS/JavaScript

## Project Structure
    final_project/
    ├── EmotionDetection/
    │   ├── init.py
    │   └── emotion_detection.py
    ├── templates/
    │   └── index.html
    ├── server.py
    └── README.md

## Steps Completed
1. Forked the repository and cloned it into `final_project` directory
2. Created the `EmotionDetection` package with `__init__.py`
3. Built the `emotion_detector` function using IBM Watson NLP API
4. Developed the Flask server (`server.py`) with emotion detection route
5. Created the web interface (`index.html`)
6. Added error handling for blank/invalid input (status code 400)
7. Added unit tests for the application
8. Applied PEP8 guidelines and achieved perfect pylint score

## How to Run
1. Clone the repository
2. Install dependencies:
```bash
   pip install flask requests
```
3. Run the application:
```bash
   python server.py
```
4. Open browser and go to `http://localhost:5000`

## Author
Payal