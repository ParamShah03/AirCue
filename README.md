GesturePlay-YT

Control YouTube videos using hand gestures with Python and OpenCV.  
No mouse, no keyboard — just your hand and a webcam.  
This project lets you play, pause, **skip**, and **adjust volume** of YouTube videos using real-time hand tracking.


How It Works

This app uses your webcam to detect hand gestures via MediaPipe and OpenCV, then simulates keyboard shortcuts (like Spacebar, Arrow keys, etc.) using PyAutoGUI to control YouTube playback.

Features

- ✋ Play/Pause with a single hand gesture          
- 🔊 Volume control by moving your hand vertically 
- ⏩ Skip forward/backward using horizontal swipes
- 🎯 Works on any YouTube video tab in the browser
- ⚡ Lightweight, fast, and easy to run

Controls
- Play/pause = Index finger
- Scroll up = Index finger + pinky finger
- Scroll down = All five fingers
- Mute = fist 
- Volume up = Thumb up
- Volume down = pinkey finger
- Mouse click = Index + middle + ring finger
- Skip/next video = Index finger + middle finger

Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- Time module (comes with Python)
