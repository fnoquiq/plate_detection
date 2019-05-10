from ImageLimitator import ImageLimitator
from ShapeDetector import ShapeDetector

import cv2


class PlateDetection:
    ShapeDetector = None
    ImageLimitator = None

    path = None
    image = None

    def __init__(self, path):
        self.path = path
        self.image = self.load_image(self.path)

        self.ImageLimitator = ImageLimitator(self.image)
        image_cuted = self.ImageLimitator.img_cuted

        self.ShapeDetector = ShapeDetector(image_cuted)

    def load_image(self, path):
        return cv2.imread(path)


detection = PlateDetection("./sample_images/positive/OJJ-3984.jpg")
cv2.imshow('Imagem com Limites', detection.ImageLimitator.img_with_limiter_indicator)
cv2.imshow('Imagem Contornada', detection.ShapeDetector.image_with_shapes)
cv2.waitKey(10000)
cv2.destroyAllWindows()
