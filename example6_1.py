# This example finds 68 face landmarks and show them 
import dlib
import cv2

detector = 'shape_predictor_68_face_landmarks.dat'
detector = dlib.shape_predictor(detector)
face_detector = dlib.get_frontal_face_detector()
mostacho = cv2.imread('images/mostacho.png', cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.pyrDown(frame)
    frame = cv2.flip(frame, 1)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detections = face_detector(img)

    for detection in detections:
        x1, y1, x2, y2 = detection.left(), detection.top(), detection.right(), detection.bottom()

        landmarks = detector(img, detection)
        landmarks_list = list(map(lambda p: (p.x, p.y), landmarks.parts()))

        for x, y in landmarks_list:
            cv2.circle(img, (x, y), 2, (255, 0, 0), -1)

    frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything's done, release the capture
cap.release()
cv2.destroyAllWindows()