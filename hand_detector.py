import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.9, maxHands=2)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    hands, img = detector.findHands(frame)

    if hands:
        for hand in hands:
            fingers = detector.fingersUp(hand)
            dirtyFingers = [fingers[i] for i in range(0, 5) if fingers[i] == 0]
            if hand["type"] == "Left":
                cv2.putText(frame, f"Left hand:{len(dirtyFingers)}", (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
                num_of_Left_hand = len(dirtyFingers)
            elif hand["type"] == "Right":
                cv2.putText(frame, f"Right hand:{len(dirtyFingers)}", (5, 65), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
                num_of_Right_hand = len(dirtyFingers)

    cv2.imshow("Hand Detector", img)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

