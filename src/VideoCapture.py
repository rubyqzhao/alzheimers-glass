import cv2

def label_face(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_PLAIN
    scale = 2
    color = (0, 0, 0)

    thickness = cv2.FILLED
    margin = 20

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)




# Create VideoCapture object that gets input from camera
cap = cv2.VideoCapture(0)

# Check if camera is working correctly
if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(True):
    ret, frame = cap.read()

    # Display the resulting frame
    if ret == True:
        # draw the label into the frame
        label_face(frame, 'Ruby Zhao', (300, 80), (255, 255, 255))
        #TODO: position should be adaptive

        # Display the resulting frame
        cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
