from abc import ABC, abstractmethod

class ImageProcessingStrategy(ABC):
    @abstractmethod
    def apply(self, image):
        pass
