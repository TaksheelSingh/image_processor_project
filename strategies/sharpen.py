import cv2
import numpy as np

class Sharpen:
    def apply(self, image):
        kernel = np.array([[0, -1, 0], 
                           [-1, 5, -1], 
                           [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)
