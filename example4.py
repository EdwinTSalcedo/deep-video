

# This example captures the image input from a camera
import cv2
import numpy as np 

# Define the input camera
camera = cv2.VideoCapture(0)

while True: 
    # Read a frame from the camera
    ret, frame = camera.read()

    # Downsample the image for faster processing
    frame = cv2.pyrDown(frame)
    frame = cv2.pyrDown(frame)

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame 
    cv2.imshow('frame',grey)

    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
camera.release()
cv2.destroyAllWindows()