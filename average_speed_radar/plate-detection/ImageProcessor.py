import cv2

from copy import copy


def __to_gray_scale_image(img_in):
    img_out = cv2.cvtColor(copy(img_in), cv2.COLOR_BGR2GRAY)
    return img_out


def __to_threshold_image(img_in):
    ret, img_out = cv2.threshold(copy(img_in), 90, 255, cv2.THRESH_BINARY)
    return img_out


def __to_blur_image(img_in):
    img_out = cv2.GaussianBlur(copy(img_in), (25, 25), 0)
    return img_out


def process_image(img_in):
    gray_scale_out_image = __to_gray_scale_image(img_in)
    threshold_out_image = __to_threshold_image(gray_scale_out_image)
    blur_out_image = __to_blur_image(threshold_out_image)

    return blur_out_image
