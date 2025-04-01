import cv2
from strategies.strategy import ImageProcessingStrategy

class EdgeDetectionStrategy(ImageProcessingStrategy):
    def apply(self, image):
        return cv2.Canny(image, 100, 200)
