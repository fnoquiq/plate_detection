from copy import copy
from plate_detection.ImageProcessor import process_image

import cv2
import numpy as np


class ShapeDetector:
    original_image = None
    cuted_image = None
    processed_image = None
    image_with_shapes = None

    image_shapes = []
    screenCnt = None

    __shapes_sides = 4
    # Select the contour with __shapes_sides corners
    __max_shapes = 10
    # Sort the contours based on area , so that the number plate-detection will be in top '__max_shapes' contours
    __perimeter_approximate = 0.06
    # Approximating with % error

    def __init__(self, original_image, cuted_image):

        self.original_image = original_image
        self.cuted_image = cuted_image

        self.processed_image = process_image(self.cuted_image)

        self.__find_shapes()
        self.__draw_shapes_in_cuted_image()

    def __find_shapes(self):

        contours, hierarchy = cv2.findContours(self.processed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:self.__max_shapes]

        for c in contours:

            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, self.__perimeter_approximate * peri, True)  # Approximating with 6% error

            if len(approx) == self.__shapes_sides:

                self.screenCnt = approx
                break

    def __draw_shapes_in_cuted_image(self):

        self.image_with_shapes = cv2.drawContours(self.cuted_image, [self.screenCnt], -1, (0, 255, 0), 3)