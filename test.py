import cv2 as cv
import buttons

### VIDEO CAPTURE ###

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # displaying video capture
    cv.imshow('Webcam', frame)
    
    # checking if user pressed quit
    if cv.waitKey(1) == ord('q'):
        break

# quit proceedure
cap.release()
cv.destroyAllWindows()