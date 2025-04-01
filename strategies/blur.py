import cv2
from strategies.strategy import ImageProcessingStrategy

class BlurStrategy(ImageProcessingStrategy):
    def apply(self, image):
        return cv2.GaussianBlur(image, (15, 15), 0)
