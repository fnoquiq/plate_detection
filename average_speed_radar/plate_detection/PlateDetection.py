from plate_detection.ImageLimitator import ImageLimitator
from plate_detection.ShapeDetector import ShapeDetector
from copy import copy

import cv2


class PlateDetection:
    ShapeDetector = None
    ImageLimitator = None

    original_image = None

    def __init__(self, img_in):
        self.original_image = img_in

        self.ImageLimitator = ImageLimitator(copy(self.original_image))
        image_cuted = self.ImageLimitator.img_cuted

        self.ShapeDetector = ShapeDetector(copy(self.original_image), image_cuted)
