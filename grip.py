import cv2
import numpy
import math
from enum import Enum

class GripPipeline:
    """
    An OpenCV pipeline generated by GRIP.
    """
    
    def __init__(self):
        """initializes all values to presets or None if need to be set
        """

        self.__cv_laplacian_ksize = 1
        self.__cv_laplacian_scale = 1.0
        self.__cv_laplacian_delta = 0.0
        self.__cv_laplacian_bordertype = cv2.BORDER_DEFAULT

        self.cv_laplacian_output = None

        self.__cv_threshold_src = self.cv_laplacian_output
        self.__cv_threshold_thresh = 50.0
        self.__cv_threshold_maxval = 50.0
        self.__cv_threshold_type = cv2.THRESH_BINARY

        self.cv_threshold_output = None


    def process(self, source0):
        """
        Runs the pipeline and sets all outputs to new values.
        """
        # Step CV_Laplacian0:
        self.__cv_laplacian_src = source0
        (self.cv_laplacian_output) = self.__cv_laplacian(self.__cv_laplacian_src, self.__cv_laplacian_ksize, self.__cv_laplacian_scale, self.__cv_laplacian_delta, self.__cv_laplacian_bordertype)

        # Step CV_Threshold0:
        self.__cv_threshold_src = self.cv_laplacian_output
        (self.cv_threshold_output) = self.__cv_threshold(self.__cv_threshold_src, self.__cv_threshold_thresh, self.__cv_threshold_maxval, self.__cv_threshold_type)


    @staticmethod
    def __cv_laplacian(src, size, scale, delta, border_type):
        """Performs a Laplacian on the image.
        Args:
            src: A numpy.ndarray.
            size: Odd number that is size of the kernel.
            scale: Scaling factor for Laplacian.
            delta: Offset for values in Laplacian.
            border_type: Opencv enum.
        Returns:
            The result as a numpy.ndarray.
        """
        return cv2.Laplacian(src, 0, ksize=(int)(size+0.5), scale=scale, delta=delta,
                            borderType=border_type)

    @staticmethod
    def __cv_threshold(src, thresh, max_val, type):
        """Apply a fixed-level threshold to each array element in an image
        Args:
            src: A numpy.ndarray.
            thresh: Threshold value.
            max_val: Maximum value for THRES_BINARY and THRES_BINARY_INV.
            type: Opencv enum.
        Returns:
            A black and white numpy.ndarray.
        """
        return cv2.threshold(src, thresh, max_val, type)[1]



