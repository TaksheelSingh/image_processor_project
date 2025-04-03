import cv2
import os
from strategies.blur import Blur
from strategies.sharpen import Sharpen
from strategies.edge_detection import EdgeDetection
from strategies.grayscale import Grayscale
from strategies.contrast import Contrast

class ImageProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, image):
        return self.strategy.apply(image)

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Error: The file '{image_path}' does not exist.")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error: Could not load the image. Check the file format and path.")
    return image

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f"Processed image saved at: {output_path}")

def get_images_from_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    images = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    return images

if __name__ == "__main__":
    input_folder = "stored_images"
    output_folder = "output"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    
    images = get_images_from_folder(input_folder)
    if not images:
        print(f"No images found in {input_folder}. Please add images and try again.")
        exit()
    
    print("Available images:")
    for idx, img in enumerate(images):
        print(f"{idx + 1}. {os.path.basename(img)}")
    
    choice_img = int(input("Select an image by entering its number: "))
    if choice_img < 1 or choice_img > len(images):
        raise ValueError("Invalid selection!")
    image_path = images[choice_img - 1]
    
    print("Choose an image processing technique:")
    print("1. Blur")
    print("2. Sharpen")
    print("3. Edge Detection")
    print("4. Grayscale")
    print("5. Contrast Enhancement")
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        processor = ImageProcessor(Blur())
        output_filename = "blurred_" + os.path.basename(image_path)
    elif choice == "2":
        processor = ImageProcessor(Sharpen())
        output_filename = "sharpened_" + os.path.basename(image_path)
    elif choice == "3":
        processor = ImageProcessor(EdgeDetection())
        output_filename = "edges_" + os.path.basename(image_path)
    elif choice == "4":
        processor = ImageProcessor(Grayscale())
        output_filename = "grayscale_" + os.path.basename(image_path)
    elif choice == "5":
        processor = ImageProcessor(Contrast())
        output_filename = "contrast_" + os.path.basename(image_path)
    else:
        raise ValueError("Invalid choice! Please select a valid option.")
    
    try:
        image = load_image(image_path)
        processed_image = processor.process(image)
        output_path = os.path.join(output_folder, output_filename)
        save_image(processed_image, output_path)
        
    except Exception as e:
        print(e)
