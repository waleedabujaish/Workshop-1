import cv2
import mediapipe as mp
import time 

# Initialize MediaPipe Pose solution
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Initialize MediaPipe drawing utilities for rendering pose landmarks
mpDraw = mp.solutions.drawing_utils

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Main loop to read and process each frame
while True:
    # Capture a frame from the webcam
    success, img = cap.read()

    # Convert the image from BGR color (OpenCV default) to RGB color
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect and obtain pose landmarks
    results = pose.process(img_rgb)

    # If pose landmarks are detected
    if results.pose_landmarks:
        # Draw the pose landmarks on the image
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
    # Display the image with pose landmarks
    cv2.imshow('Image', img)

    # Break out of the loop if the 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
