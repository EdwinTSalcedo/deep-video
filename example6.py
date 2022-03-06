# This example captures the image input from a camera
import cv2
import numpy as np 
from skimage.feature import match_template

# Define the input camera
camera = cv2.VideoCapture(0)

# Import the templates
like = cv2.imread('images/like.jpeg')
dislike = cv2.imread('images/dislike.jpeg')

# Import the emojis
like_emoji = cv2.imread('images/like_emoji.jpeg')
dislike_emoji = cv2.imread('images/dislike_emoji.jpeg')

like = cv2.pyrDown(cv2.pyrDown(like))
dislike = cv2.pyrDown(cv2.pyrDown(like))
like_emoji = cv2.pyrDown(cv2.pyrDown(like_emoji))
dislike_emoji = cv2.pyrDown(cv2.pyrDown(dislike_emoji))

# Convert to grayscale
like = cv2.cvtColor(like, cv2.COLOR_BGR2GRAY)
dislike = cv2.cvtColor(dislike, cv2.COLOR_BGR2GRAY)

# templates = [like,dislike]

def match_emoji(grayscale, frame, template, emoji):
    result = match_template(grayscale, template)

    threshold = 0.70

    max_corr = np.max(result)

    if max_corr > threshold:
        # Find the index of the highest value in the matrix
        ij = np.unravel_index(np.argmax(result), result.shape)
        x, y = ij[::-1]

        # Find the template's shape
        template_rows, template_cols = template.shape

        # Define position for the emojis
        x_offset=y_offset=20

        frame[y_offset:y_offset+emoji.shape[0], x_offset:x_offset+emoji.shape[1]] = emoji
    
    return frame

while True: 
    ret, frame = camera.read()

    # Downsample the frame for faster processing
    frame = cv2.pyrDown(cv2.pyrDown(frame))

    # Convert to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = match_emoji(grayscale,frame, like, like_emoji)
    frame = match_emoji(grayscale,frame, dislike, dislike_emoji)

    # Display the frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
cap.release()
cv2.destroyAllWindows()