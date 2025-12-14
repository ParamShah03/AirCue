import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import time
import platform
import subprocess
import screen_brightness_control as sbc

# Open YouTube in default browser
webbrowser.open("https://www.youtube.com")
time.sleep(5)

# Hand detection setup
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]  # [thumb, index, middle, ring, pinky] tips

OS_NAME = platform.system()  # 'Darwin' for macOS, 'Windows', 'Linux', etc.

def brightness_up():
    try:
        if OS_NAME == "Darwin":
            # macOS: simulate hardware Brightness Up key
            subprocess.run(
                ["osascript", "-e",
                 'tell application "System Events" to key code 145'],
                check=False
            )
        else:
            # Windows / Linux: use screen_brightness_control
            import screen_brightness_control as sbc
            current_level = sbc.get_brightness(display=0)[0]
            sbc.set_brightness(min(current_level + 10, 100), display=0)
    except Exception as e:
        print("Brightness error (up):", e)


def brightness_down():
    try:
        if OS_NAME == "Darwin":
            # macOS: simulate hardware Brightness Down key
            subprocess.run(
                ["osascript", "-e",
                 'tell application "System Events" to key code 144'],
                check=False
            )
        else:
            import screen_brightness_control as sbc
            current_level = sbc.get_brightness(display=0)[0]
            sbc.set_brightness(max(current_level - 10, 0), display=0)
    except Exception as e:
        print("Brightness error (down):", e)


def fingers_up(lmList):
    """
    Returns a list of 5 ints [thumb, index, middle, ring, pinky]
    1 = finger up, 0 = finger down
    """
    fingers = []

    # Thumb: compare x-coordinates (since hand is flipped horizontally)
    if lmList[tip_ids[0]][1] > lmList[tip_ids[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers: compare y-coordinates (tip higher than lower joint)
    for id in range(1, 5):
        if lmList[tip_ids[id]][2] < lmList[tip_ids[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    lmList = []
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            draw.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)

        if lmList:
            fingers = fingers_up(lmList)
            # Debug: show finger pattern on screen
            cv2.putText(img, str(fingers), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Play / Pause: only index up
            if fingers == [0, 1, 0, 0, 0]:
                pyautogui.press("space")
                cv2.putText(img, "Play/Pause", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                time.sleep(1)

            # Skip forward: index + middle up
            elif fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("right")
                cv2.putText(img, "Seek >>", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                time.sleep(1)

            # Volume up: thumb only
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("volumeup")
                cv2.putText(img, "Volume +", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                time.sleep(0.5)

            # Volume down: pinky only
            elif fingers == [0, 0, 0, 0, 1]:
                pyautogui.press("volumedown")
                cv2.putText(img, "Volume -", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                time.sleep(0.5)

            # Mute: fist
            elif fingers == [0, 0, 0, 0, 0]:
                pyautogui.press("m")
                cv2.putText(img, "Mute", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                time.sleep(1)

            # Scroll down: all fingers up
            elif fingers == [1, 1, 1, 1, 1]:
                pyautogui.scroll(-300)
                cv2.putText(img, "Scroll Down", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                time.sleep(0.5)

            # Scroll up: index + pinky
            elif fingers == [0, 1, 0, 0, 1]:
                pyautogui.scroll(300)
                cv2.putText(img, "Scroll Up", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                time.sleep(0.5)

            # Click: index + middle + ring
            elif fingers == [0, 1, 1, 1, 0]:
                pyautogui.click()
                cv2.putText(img, "Click", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                time.sleep(0.5)

            # 🔆 Brightness UP: thumb + index up (others down)
            elif fingers == [1, 1, 0, 0, 0]:
                brightness_up()
                cv2.putText(img, "Brightness +", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                time.sleep(0.7)

            # 🔅 Brightness DOWN: thumb + index + middle up
            elif fingers == [1, 1, 1, 0, 0]:
                brightness_down()
                cv2.putText(img, "Brightness -", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                time.sleep(0.7)

    cv2.imshow("Gesture Controller", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
