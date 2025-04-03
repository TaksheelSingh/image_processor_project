import cv2
import numpy as np

class Contrast:
    def apply(self, image):
        alpha = 1.5  # Contrast control (1.0 - 3.0)
        beta = 20    # Brightness control (0 - 100)
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
