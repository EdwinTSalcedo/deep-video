# IMPORTANT: Install opencv with 'pip install opencv-python'

# This example explains how to open a video located in the same directory 
import numpy as np
import cv2

# Define the name of the video file
video = cv2.VideoCapture('videos/ball.mp4')

print(video.get(0))

# Iterate over all frames in the video
while(video.isOpened()):
    # Read the video frame by frame. the variable ret contains a boolean value which states 
    # if there is a frame or not. 
    ret, frame = video.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame
    cv2.imshow('frame',gray)

    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Close the connection with the opened video and destroy all windows
video.release()
cv2.destroyAllWindows()


# IMPORTANT: Possible properties (metadata) available with cv2.VideoCapture.get(x)
# cv2.VideoCapture.get(0)	CV_CAP_PROP_POS_MSEC The current position (play) of the video file in milliseconds
# cv2.VideoCapture.get(1)	CV_CAP_PROP_POS_FRAMES is based on0The index of the first captured or decoded frame
# cv2.VideoCapture.get(2)	CV_CAP_PROP_POS_AVI_RATIO relative position of the video file (play):0=The movie begins,1=The end of the movie.
# cv2.VideoCapture.get(3)	CV_CAP_PROP_FRAME_WIDTH the width of the frame in the video stream
# cv2.VideoCapture.get(4)	CV_CAP_PROP_FRAME_HEIGHT is the height of the frame of the video stream
# cv2.VideoCapture.get(5)	CV_CAP_PROP_FPS frame rate
# cv2.VideoCapture.get(6)	CV_CAP_PROP_FOURCC codec4word-Character code
# cv2.VideoCapture.get(7)	CV_CAP_PROP_FRAME_COUNT The number of frames in the video file
# cv2.VideoCapture.get(8)	CV_CAP_PROP_FORMAT returns the format of the object
# cv2.VideoCapture.get(9)	CV_CAP_PROP_MODE returns a back-end specific value, which indicates the current capture mode
# cv2.VideoCapture.get(10)	 CV_CAP_PROP_BRIGHTNESS image brightness(Only for camera)
# cv2.VideoCapture.get(11)	CV_CAP_PROP_CONTRAST image contrast(Only for camera)
# cv2.VideoCapture.get(12)	CV_CAP_PROP_SATURATION image saturation(Only for camera)
# cv2.VideoCapture.get(13)	CV_CAP_PROP_HUE tone image(Only for camera)
# cv2.VideoCapture.get(14)	CV_CAP_PROP_GAIN image gain(Only for camera)(Gain means white balance improvement in photography)
# cv2.VideoCapture.get(15)	CV_CAP_PROP_EXPOSURE exposure(Only for camera)
# cv2.VideoCapture.get(16)	CV_CAP_PROP_CONVERT_RGB indicates whether the image should be converted to RGB Boolean flag
# cv2.VideoCapture.get(17)	CV_CAP_PROP_WHITE_BALANCE × Not currently supported
# cv2.VideoCapture.get(18)	CV_CAP_PROP_RECTIFICATION The correction mark of the stereo camera (currently only DC1394 v.2.x backend supports this function)
