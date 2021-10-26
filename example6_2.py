import dlib
import cv2
import imutils
import math

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

    if len(detections) > 0:

        size_offset = 50
        alpha_img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

        for detection in detections:
            x1, y1, x2, y2 = detection.left(), detection.top(), detection.right(), detection.bottom()

            landmarks = detector(img, detection)
            landmarks_list = list(map(lambda p: (p.x, p.y), landmarks.parts()))

            # Centers
            y_position = (landmarks_list[51][1] + landmarks_list[33][1]) // 2
            x_position = landmarks_list[51][0]

            # Angle
            (xl, yt), (xr, yb) = landmarks_list[48], landmarks_list[54]
            xl -= size_offset
            xr += size_offset
            # angle = math.degrees(math.atan((yb - yt) / (xr - xl)))
            angle = math.degrees(math.atan(
                (landmarks_list[2][1] - landmarks_list[14][1]) / (landmarks_list[2][0] - landmarks_list[14][0])))

            # Rotate
            small_mostacho = imutils.resize(mostacho, width=xr - xl)
            small_mostacho = imutils.rotate_bound(small_mostacho, angle)
            
            # Alpha Channel
            alpha_s = small_mostacho[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            # Merge
            for c in range(3):
                left = x_position - small_mostacho.shape[1] // 2
                right = left + small_mostacho.shape[1]

                top = y_position - small_mostacho.shape[0] // 2
                bottom = top + small_mostacho.shape[0]

                alpha_img[top:bottom, left:right, c] = (alpha_s * small_mostacho[:, :, c] +
                                                        alpha_l * alpha_img[top:bottom, left:right, c])

        frame = cv2.cvtColor(alpha_img, cv2.COLOR_RGBA2BGR)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()