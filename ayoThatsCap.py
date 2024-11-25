import cv2 as cv

### VIDEO CAPTURE ###
cap = cv.VideoCapture(0)

def getCap():
    shouldBreak = False

    r, frame = cap.read()
    
    # checking if user pressed quit
    if cv.waitKey(1) == ord('q'):
        shouldBreak = True
        cap.release()

    return frame, shouldBreak