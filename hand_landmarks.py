import cv2
import mediapipe as mp
import time 

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize mediapipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# Initialize drawing utility for landmarks
mpDraw = mp.solutions.drawing_utils

# Variables to calculate frames per second (FPS)
pTime = 0
cTime = 0

# Main loop to continuously capture frames from the webcam
while True:
    # Read a frame from the webcam
    success, img = cap.read()

    # Convert the image from BGR to RGB as mediapipe expects RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hands and their landmarks
    results = hands.process(img_rgb)

    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        # Iterate over detected hands
        for handLms in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # Display FPS on the image
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    # Display the image
    cv2.imshow('Image', img)

    # Break the loop if 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
