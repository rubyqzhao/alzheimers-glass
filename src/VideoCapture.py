import cv2


def identify_face(frame):
    print("Found face")


def label_face(img, text):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    label_color = (0, 255, 0)
    line_thickness = 2
    scale_factor = 1.2
    min_neighbors = 5

    # Use Haar cascading method to find faces
    haar_cascade_face = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')

    # Convert to gray image for faster video processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_rects = haar_cascade_face.detectMultiScale(gray, scale_factor, min_neighbors)

    # Draw box around detected face
    for (x, y, w, h) in faces_rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), label_color, line_thickness)
        cv2.putText(img, text, (x, y-10), font_face, font_scale, label_color, font_thickness, cv2.LINE_AA)

cap = cv2.VideoCapture(0)

# Check if camera is working correctly
if not cap.isOpened():
  print("Error opening video stream or file")

while(True):
    ret, frame = cap.read()

    if ret == True:
        #while API hasn't returned
        label_face(frame, 'Detecting face...')
        #else
        #label_face(frame, 'This is {0}, your {1}.'.format(name, relation))

        cv2.imshow('Alzheimers Glasses Demo', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('i'):
        identify_face(frame)
    elif key == ord('q'):
        break


# When done, release the capture
cap.release()
cv2.destroyAllWindows()
