import cv2

from plate_detection.PlateDetection import PlateDetection

detection = PlateDetection("./plate_detection/sample_images/positive/OJJ-3984.jpg")
cv2.imshow('Imagem com Limites', detection.ImageLimitator.img_with_limiter_indicator)
cv2.imshow('Imagem Contornada', detection.ShapeDetector.image_with_shapes)
cv2.waitKey(10000)
cv2.destroyAllWindows()
