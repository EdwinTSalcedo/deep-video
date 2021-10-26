# This example captures the image input from a camera
import cv2
import numpy as np 

camera = cv2.VideoCapture(0)

while True: 
    ret, frame = camera.read()

    # # Downsample the image for faster processing
    frame = cv2.pyrDown(frame)
    frame = cv2.pyrDown(frame)

    # Convert to grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a binary thresholded image
    retval, binary = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours from thresholded, binary image
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw all contours on a copy of the original image
    contours_image = np.copy(frame)
    for c in contours:
        cv2.drawContours(contours_image, c, -1, (0,255,0), 1)

    cv2.imshow('contours_image',contours_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
camera.release()
cv2.destroyAllWindows()