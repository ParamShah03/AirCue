Here’s an updated README you can copy-paste and tweak as needed:

---

# AirCue (GesturePlay-YT)

Control YouTube videos and screen brightness using **mid-air hand gestures** with Python and OpenCV.
No mouse, no keyboard — just your hand and a webcam.

This project uses a standard laptop webcam plus MediaPipe Hands to track your fingers in real time and sends keyboard / mouse events (via PyAutoGUI) to control YouTube and OS brightness.

---

## How It Works

1. Webcam captures frames of your hand.
2. MediaPipe Hands detects 21 hand landmarks.
3. A small rule-based engine decides which fingers are **up** or **down**.
4. Each finger pattern is mapped to a gesture (play/pause, seek, scroll, volume, brightness).
5. PyAutoGUI sends the corresponding key or mouse event to the active browser window, and a small brightness module talks to the OS to change screen brightness.

Runs in real time on a single laptop with built-in webcam.

---

## Features

* ✋ **Play/Pause** YouTube with a simple finger pose
* ⏩ **Seek / skip** using a two-finger gesture
* 🔊 **System volume** up/down using thumb and pinky
* 🌞 **Screen brightness** up/down using thumb + index combos
* 🖱️ **Scroll and click** using multi-finger poses
* 🎥 Works with any YouTube tab in a standard desktop browser
* ⚡ Lightweight, rule-based, and easy to understand / modify

---

## Gesture Controls

Finger order: **[thumb, index, middle, ring, pinky]**

| Gesture / Action    | Hand Pose (intuitive description) |
| ------------------- | --------------------------------- |
| Play / Pause        | **Index only** up                 |
| Seek forward (skip) | **Index + middle** up             |
| Volume up           | **Thumb only** up                 |
| Volume down         | **Pinky only** up                 |
| Mute / Unmute       | **Fist** (all fingers folded)     |
| Scroll down         | **All five fingers** up           |
| Scroll up           | **Index + pinky** up              |
| Mouse click         | **Index + middle + ring** up      |
| Brightness up       | **Thumb + index** up              |
| Brightness down     | **Thumb + index + middle** up     |

> Tip: keep your hand roughly at chest / shoulder height, facing the camera.

---

## Requirements

* Python **3.8+**
* [OpenCV](https://pypi.org/project/opencv-python/)
* [MediaPipe](https://pypi.org/project/mediapipe/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* `screen_brightness_control` (for brightness on Windows/Linux) or AppleScript (macOS)
* Standard laptop / USB webcam

Install (example):

```bash
pip install opencv-python mediapipe pyautogui screen_brightness_control
```

---

## How to Run

1. Open a YouTube video in your browser and make sure the tab is **active**.
2. Run the gesture controller:

```bash
python GesturePlay-YT.py
```

3. Move your hand into the webcam view and try the gestures from the table above.
4. Watch the on-screen overlay (finger vector + action label) to see how the system is interpreting your pose.

---

## Notes

* On macOS you may need to grant **Accessibility** permission for Python / your terminal so PyAutoGUI can send key presses.
* Brightness control may not work on all external monitors; it is best tested on a laptop’s built-in display.
* This is a research / prototype project for an HCI course, not a polished product — expect a few false recognitions and adjust gestures accordingly.
