# This example captures the image input from a camera
import cv2
import numpy as np 

# Define the input camera
video = cv2.VideoCapture('videos/laguna-colorada.mp4')
fps = video.get(cv2.CAP_PROP_FPS)

while(video.isOpened()):
    # Read a frame from the camera
    ret, frame = video.read()

    # Downsample the image for faster processing
    frame = cv2.pyrDown(frame)
    frame = cv2.pyrDown(frame)

    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # Get borders
    edges = cv2.Canny(grey,100,200)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    # Add two images (base image and its version with edges), where 1 and 0.5 determine the weighting. 
    combined = cv2.addWeighted(frame,1,edges,0.5,0)
    # Show the frame 
    cv2.imshow('frame',combined)
    delay = int( (1 / int(fps)) * 500)
    cv2.waitKey(delay)
    
    
    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
camera.release()
cv2.destroyAllWindows()
