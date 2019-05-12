from plate_detection.ImageLimitator import ImageLimitator
from plate_detection.ShapeDetector import ShapeDetector

import cv2


class PlateDetection:
    ShapeDetector = None
    ImageLimitator = None

    path = None
    original_image = None

    def __init__(self, path):
        self.path = path
        self.original_image = self.load_image(self.path)

        self.ImageLimitator = ImageLimitator(self.original_image)
        image_cuted = self.ImageLimitator.img_cuted

        self.ShapeDetector = ShapeDetector(self.original_image, image_cuted)

    def load_image(self, path):
        return cv2.imread(path)
