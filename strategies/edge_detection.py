import cv2

class EdgeDetection:
    def apply(self, image):
        return cv2.Canny(image, 100, 200)
