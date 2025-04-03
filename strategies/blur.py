import cv2

class Blur:
    def apply(self, image):
        return cv2.GaussianBlur(image, (15, 15), 0)
