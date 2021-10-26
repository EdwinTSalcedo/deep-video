# This example explains how to find matches with an image template 
import numpy as np
import cv2
from skimage.feature import match_template

# Define the name of the video file
video = cv2.VideoCapture('videos/ball.mp4')

# Import the template
template = cv2.imread('images/template.jpg')
# Convert to grayscale
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# Find the shape
template_rows, template_cols = template.shape

# Iterate over all frames in the video
while(video.isOpened()):
    # Read the video frame by frame. the variable ret contains a boolean value which states 
    # if there is a frame or not. 
    ret, frame = video.read()

    # Copy frame to process a grayscale version
    grayscale = np.copy(frame)
    grayscale = cv2.cvtColor(grayscale, cv2.COLOR_BGR2GRAY)

    # Find matches using FFTs
    result = match_template(grayscale, template)

    cv2.imshow('result',result)

    # Find the index of the highest value in the matrix
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]

    # Draw a rectangle where there is a match
    cv2.rectangle(frame, (x, y), (x+template_cols, y+template_rows), (255,0,0), 2)

    # Display the frame
    cv2.imshow('frame',frame)

    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the connection with the opened video and close all windows
video.release()
cv2.destroyAllWindows()