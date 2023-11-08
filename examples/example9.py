from ultralytics import YOLO
import cv2
import pandas as pd

# Load model
model = YOLO('../models/yolov8n.pt')

# Define the input camera
camera = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX 

color = (252, 100, 2)

while True: 
    # Read a frame from the camera
    ret, frame = camera.read()

    # Inference
    results = model(frame)

    for detections in results[0].boxes:
        # Obtain the label per n bboxes
        label = model.names[int(detections.cls)]
        # Obtain and draw each bounding box with respect to a label
        for bbox in detections.xyxy.cpu().numpy():
            xmin = int(bbox[0])
            ymin = int(bbox[1])
            xmax = int(bbox[2])
            ymax = int(bbox[3])

            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
            
            if xmin == 0:xmin +=40
            if ymin == 0:ymin +=40
        
            cv2.putText(frame, label, (xmin, ymin), font,
                        fontScale=2, color=color, thickness=2, lineType=cv2.LINE_AA) 
    
        
    cv2.imshow('frame', frame)
    
    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
camera.release()
cv2.destroyAllWindows()