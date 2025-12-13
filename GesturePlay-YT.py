import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import time

# Open YouTube
webbrowser.open("https://www.youtube.com")
time.sleep(5)

# Hand detection setup
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]

def fingers_up(lmList):
    fingers = []
    if lmList[tip_ids[0]][1] > lmList[tip_ids[0] - 1][1]:
        fingers.append(1)  
    else:
        fingers.append(0)
    for id in range(1, 5):
        if lmList[tip_ids[id]][2] < lmList[tip_ids[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
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

            if fingers == [0, 1, 0, 0, 0]:  
                pyautogui.press("space")  
                time.sleep(1)

            elif fingers == [0, 1, 1, 0, 0]:  
                pyautogui.press("right")  
                time.sleep(1)

            elif fingers == [1, 0, 0, 0, 0]:  
                pyautogui.press("volumeup")
                time.sleep(0.5)

            elif fingers == [0, 0, 0, 0, 1]:  
                pyautogui.press("volumedown")
                time.sleep(0.5)

            elif fingers == [0, 0, 0, 0, 0]:  
                pyautogui.press("m")  
                time.sleep(1)

            elif fingers == [1, 1, 1, 1, 1]:  
                pyautogui.scroll(-300)  
                time.sleep(0.5)

            elif fingers == [0, 1, 0, 0, 1]:  
                pyautogui.scroll(100)  
                time.sleep(0.5)

            elif fingers == [0, 1, 1, 1, 0]:  
                pyautogui.click()  
                time.sleep(0.5)

    cv2.imshow("Gesture Controller", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
