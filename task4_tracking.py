import cv2 
from ultralytics import YOLO 
 
# Load the pre-trained YOLOv8 model (it will download automatically the first time) 
model = YOLO('yolov8n.pt')  
 
# Set up real-time video input (0 is usually the default laptop webcam) 
cap = cv2.VideoCapture(0) 
 
print("Starting video stream. Press 'q' to quit.") 
 
while cap.isOpened(): 
    success, frame = cap.read() 
     
    if success: 
        # Run YOLOv8 tracking on the frame, persisting tracks between frames 
        # This applies both object detection and object tracking natively 
        results = model.track(frame, persist=True, tracker="botsort.yaml") 
         
        # Visualize the results on the frame (draws boxes, labels, and tracking IDs) 
        annotated_frame = results[0].plot() 
         
        # Display the output 
        cv2.imshow("Task 4: Object Detection and Tracking", annotated_frame) 
         
        # Break loop if 'q' is pressed 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
    else: 
        break 
 
# Release the video capture object and close display window 
cap.release() 
cv2.destroyAllWindows()
