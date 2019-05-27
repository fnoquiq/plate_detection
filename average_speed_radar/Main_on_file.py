import  cv2
from plate_detection.ImageProcessor import process_image

while True:

    frame = cv2.imread("./plate_detection/sample_images/positive/BAG-7751.jpg")
    process_image(frame)

    if cv2.waitKey(1) == ord('q'):
        break