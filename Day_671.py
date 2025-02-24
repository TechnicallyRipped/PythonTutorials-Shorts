
# pip install opencv-python
import cv2

cam = cv2.VideoCapture(0)

while True: 
    successful, frame = cam.read()
    if not successful:
          break
    cv2.imshow("Live Webcam Feed", frame)
    if cv2.waitKey(1) == ord('q'):
            break

cam.release() 
cv2.destroyAllWindows()

