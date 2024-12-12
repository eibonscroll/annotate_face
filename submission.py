import cv2
import math

# Lists to store the points
center=[]
circumference=[]

def drawBoundingBox(action, x, y, flags, userdata):
    global center, circumference
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]
    elif action == cv2.EVENT_LBUTTONUP:
        circumference = [(x, y)]
        top_left = (min(center[0][0], circumference[0][0]), min(center[0][1], circumference[0][1]))
        bottom_right = (max(center[0][0], circumference[0][0]), max(center[0][1], circumference[0][1]))
        cv2.rectangle(source, top_left, bottom_right, (0, 255, 0), 2)
        cv2.imshow("Window", source)

        # Crop the region inside the bounding box
        cropped_face = source[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

        # Save the cropped face
        cv2.imwrite('cropped_face.jpg', cropped_face)

source = cv2.imread("./data/JCarmack.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawBoundingBox)
k = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", source)
    cv2.putText(source,'''Choose center, and drag, 
                      Press ESC to exit and c to clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
              0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k==99:
        source= dummy.copy()


cv2.destroyAllWindows()