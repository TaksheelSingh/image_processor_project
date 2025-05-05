from PIL import Image
from abc import ABC, abstractmethod

class ImageProcessingStrategy(ABC):
    @abstractmethod
    def apply(self, image: Image.Image) -> Image.Image:
        pass
