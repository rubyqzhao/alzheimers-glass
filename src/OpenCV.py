import cv2

#creates variable that reads lena.jpg
img = cv2.imread('lena.jpg', 0)

print(img)

#shows lena.jpg in a window called image
cv2.imshow('image', img)
k = cv2.waitKey(0)

#makes copy of lena.jpg when the "s" key is pressed
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg', img)
cv2.destroyAllWindows()
