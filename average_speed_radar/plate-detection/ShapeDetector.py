from copy import copy
from ImageProcessor import process_image

import cv2


class ShapeDetector:

    image_in = None
    image_processed = None
    image_with_shapes = None

    image_shapes = []

    __shapes = None
    __shapes_sides = 3
    __perimeter_limit = 80
    __perimeter_approximate = 0.3

    def __init__(self, img_in):
        self.img_in = img_in

        self.image_processed = process_image(self.img_in)

        self.find_contours(self.image_processed)
        self.image_with_shapes = self.__draw_shapes(self.img_in)

    def find_contours(self, image):
        self.__shapes, hier = cv2.findContours(copy(image), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    def __draw_shapes(self, image_in):
        img_with_shapes = copy(image_in)

        for shape in self.__shapes:

            perimeter = cv2.arcLength(shape, True)
            if perimeter > self.__perimeter_limit:
                approx = cv2.approxPolyDP(shape, self.__perimeter_approximate * perimeter, True)

                if len(approx) == self.__shapes_sides:

                    cv2.drawContours(img_with_shapes, [shape], -1, (0, 255, 0), 1)
                    (x, y, a, l) = cv2.boundingRect(shape)
                    cv2.rectangle(img_with_shapes, (x, y), (x + a, y + l), (0, 255, 0), 2)
                    roi = img_with_shapes[y:y + l, x:x + a]

                    self.image_shapes.append(roi)

        return img_with_shapes
