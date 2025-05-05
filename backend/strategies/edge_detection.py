import cv2
import numpy as np
from PIL import Image
from strategies.strategy import ImageProcessingStrategy

class EdgeDetectionStrategy(ImageProcessingStrategy):
    def apply(self, image):
        image_np = np.array(image)
        image_gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(image_gray, 100, 200)
        return Image.fromarray(edges)
