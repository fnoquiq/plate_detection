from plate_detection.ImageLimitator import ImageLimitator
from plate_detection.ShapeDetector import ShapeDetector
from copy import copy

import cv2


class PlateDetection:
    image_limitator_active = False

    ShapeDetector = None
    ImageLimitator = None

    original_image = None
    image_cuted = None

    def __init__(self, img_in):
        self.original_image = img_in

        self.ImageLimitator = ImageLimitator(copy(self.original_image))
        self.image_cuted = self.ImageLimitator.img_cuted

        if self.image_limitator_active is True:
            self.ShapeDetector = ShapeDetector(copy(self.original_image), self.image_cuted)
        else:
            self.ShapeDetector = ShapeDetector(copy(self.original_image), self.original_image)
