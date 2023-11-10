import torch
import cv2

# Check if Yolov5 is available on the computer
# torch.cuda.is_available()

# Load model. Note that ultralytics/yolov5:v7.0 defines a pinned Yolov5 version available on the PyTorch Hub. 
# model = torch.hub.load('ultralytics/yolov5:v7.0', 'yolov5m')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('ultralytics/yolov5:v7.0', 'custom', '../models/yolov5m.pt')  # custom trained model

# Define the input camera
camera = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX 

color = (252, 100, 2)

while True: 
    # Read a frame from the camera
    ret, frame = camera.read()

    # Inference
    results = model(frame)

    # print(results.xyxy[0])  # obtain frame predictions (PyTorch tensor)
    # print(results.pandas().xyxy[0])  # obtain frame predictions (pandas dataframe)

    # Draw bounding boxes on image 
    for idx, bbox in results.pandas().xyxy[0].iterrows():   
        xmin = int(bbox["xmin"])
        xmax = int(bbox["xmax"])
        ymin = int(bbox["ymin"])
        ymax = int(bbox["ymax"])

        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)

        if xmin == 0:xmin +=40
        if ymin == 0:ymin +=40
        
        cv2.putText(frame, bbox["name"], (xmin, ymin), font,  
                   fontScale=2, color=color, thickness=2, lineType=cv2.LINE_AA) 
    
    cv2.imshow('frame', frame)
    
    # waitkey(1) defines the video velocity where 1 is normal, 25 would be slow.
    # 0xFF captures a pressed key 'q' so that the video stops
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera connection and all windows
camera.release()
cv2.destroyAllWindows()