from copy import copy

import cv2


class ImageLimitator:
    img_in = None

    first_line_height = 200
    first_line_width = 200
    second_line_width = 500

    img_with_limiter_indicator = None
    img_cuted = None

    def __init__(self, img_in):
        self.img_in = img_in
        self.preview_cut()
        self.cut_image()

    def cut_image(self):
        self.img_cuted = self.img_in[self.first_line_height:, self.first_line_width:self.second_line_width]

    def preview_cut(self):
        height, width, channels = self.img_in.shape
        self.img_with_limiter_indicator = copy(self.img_in)

        self.img_with_limiter_indicator = cv2.line(
            self.img_with_limiter_indicator,
            (0, self.first_line_height),
            (width, self.first_line_height),
            (0, 0, 255),
            1
        )

        self.img_with_limiter_indicator = cv2.line(
            self.img_with_limiter_indicator,
            (self.first_line_width, width),
            (self.first_line_width, 0),
            (0, 0, 255),
            1
        )

        self.img_with_limiter_indicator = cv2.line(
            self.img_with_limiter_indicator,
            (self.second_line_width, width),
            (self.second_line_width, 0),
            (0, 0, 255),
            1
        );
