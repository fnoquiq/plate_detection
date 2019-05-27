import cv2
import numpy as np

from copy import copy


def __to_gray_scale_image(img_in):
    img_out = cv2.cvtColor(copy(img_in), cv2.COLOR_BGR2GRAY)
    return img_out


def __remove_noise_on_image(img_in):
    img_out = cv2.bilateralFilter(img_in, 9, 75, 75)
    return img_out


def __histogram_equalisation_on_image(img_in):
    img_out = cv2.equalizeHist(img_in)
    return img_out


def __to_threshold_image(img_in):
    ret, img_out = cv2.threshold(copy(img_in), 90, 255, cv2.THRESH_BINARY)
    return img_out


def __morphological_opening_image(histogram_equalized):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morph_image = cv2.morphologyEx(histogram_equalized, cv2.MORPH_OPEN, kernel, iterations=15)
    return morph_image


def __subtract_image(equal_histogram, morph_image):
    img_out = cv2.subtract(equal_histogram, morph_image)
    return img_out


def __blur_image(img_in):
    img_out = cv2.GaussianBlur(copy(img_in), (25, 25), 0)
    return img_out


def __canny_image(img_in):
    img_out = cv2.Canny(img_in, 250, 255)
    return img_out


def __dilate_shapes_on_image(img_in):
    kernel = np.ones((3, 3), np.uint8)
    img_out = cv2.dilate(img_in, kernel, iterations=1)
    return img_out


def process_image(img_in):
    # cv2.imshow('img_in', img_in)

    gray_scale_out_image = __to_gray_scale_image(img_in)
    # cv2.imshow('gray_scale_out_image', gray_scale_out_image)

    remove_noise = __remove_noise_on_image(gray_scale_out_image)
    # cv2.imshow('remove_noise', remove_noise)

    equal_histogram = __histogram_equalisation_on_image(remove_noise)
    # cv2.imshow('equal_histogram', equal_histogram)

    morph_image = __morphological_opening_image(equal_histogram)
    # cv2.imshow('morph_image', morph_image)

    subtracted_image = __subtract_image(equal_histogram, morph_image)
    # cv2.imshow('subtracted_image', subtracted_image)

    threshold_out_image = __to_threshold_image(subtracted_image)
    # cv2.imshow('threshold_out_image', threshold_out_image)

    # blur_out_image = __blur_image(threshold_out_image)

    canny_image = __canny_image(threshold_out_image)
    # cv2.imshow('canny_image', canny_image)

    dilated_image = __dilate_shapes_on_image(canny_image)
    # cv2.imshow('dilated', dilated_image)

    return dilated_image
