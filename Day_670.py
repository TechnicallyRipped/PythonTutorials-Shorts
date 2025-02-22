

# pip install opencv-python
import cv2

cam = cv2.VideoCapture(0)

successful, frame = cam.read()

if successful:
    cv2.imwrite("python_pic.png", frame)
    print('Picture taken and saved')
else:
    print('No picture taken.')

cam.release() 
cv2.destroyAllWindows()

