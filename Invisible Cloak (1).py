import cv2
import numpy as np
import time

# Start the webcam
cap = cv2.VideoCapture(0)
time.sleep(3)

# Capture background
background_frame = None # Initialize to None
for i in range(30):
    ret, frame = cap.read()
    if ret:
        background_frame = frame # Store the successfully read frame
    else:
        # If a read fails, print a warning but continue attempting to get a frame
        print(f"Warning: Failed to read frame {i+1} during background capture.")
        # If camera is completely unavailable, all 30 reads will fail.
        # In that case, background_frame will remain None.

# Check if a valid frame was ever captured for background
if background_frame is None:
    print("Error: Unable to capture any background frame. Please ensure your webcam is connected and accessible.")
    cap.release()
    cv2.destroyAllWindows()
    raise RuntimeError("Failed to capture background from webcam.")

background = np.flip(background_frame, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame during main loop. Exiting.")
        break

    frame = np.flip(frame, axis=1)

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color range for red cloak (tune according to cloth)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    # Create inverse mask
    mask_inv = cv2.bitwise_not(mask)

    # Segment the cloak area
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Segment everything except the cloak
    rest = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Final output
    final = cv2.addWeighted(cloak_area, 1, rest, 1, 0)

    cv2.imshow("Invisible Cloak Effect", final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
