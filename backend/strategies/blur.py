import cv2
import numpy as np
from PIL import Image
from strategies.strategy import ImageProcessingStrategy

class BlurStrategy(ImageProcessingStrategy):
    def apply(self, image):
        image_np = np.array(image)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        blurred = cv2.GaussianBlur(image_bgr, (15, 15), 0)
        image_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)
        return Image.fromarray(image_rgb)
