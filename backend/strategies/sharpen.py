import cv2
import numpy as np
from PIL import Image
from strategies.strategy import ImageProcessingStrategy

class SharpenStrategy(ImageProcessingStrategy):
    def apply(self, image):
        image_np = np.array(image)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
        sharpened = cv2.filter2D(image_bgr, -1, kernel)
        image_rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)
        return Image.fromarray(image_rgb)
