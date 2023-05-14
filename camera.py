import cv2
import datetime

# Set the camera device id. Usually, the default id is 0 for the first connected USB camera
camera_id = 0

# Set the video output file name
output_file = "output_video.avi"

# Initialize the camera
cap = cv2.VideoCapture(camera_id)

# Get the width and height of the video frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, 30, (frame_width, frame_height))

while cap.isOpened():
    # Capture each frame
    ret, frame = cap.read()
    
    if ret:
        # Display the frame in a window
        cv2.imshow("Camera Stream", frame)

        # Save the frame to the output video file
        out.write(frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the camera and output file
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
