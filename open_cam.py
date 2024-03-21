# Import the necessary libraries
import cv2  # OpenCV for image and video processing
import mediapipe as mp  # MediaPipe for efficient image processing
import time  # Time module to handle time-related tasks

# Start capturing video from the webcam (device 0 by default)
cap = cv2.VideoCapture(0)

# Continuously read frames from the webcam
while True:
    # Read a frame from the video capture object
    success, img = cap.read()  # 'success' is a boolean indicating if the frame was read correctly

    # Display the captured image in a window named 'Image'
    cv2.imshow('Image', img)

    # Wait for 1 ms before moving to the next frame and check if the user pressed the ESC key (key code 27)
    key = cv2.waitKey(1)
    if key == 27:  # If ESC is pressed, break out of the loop
        break
    
# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
