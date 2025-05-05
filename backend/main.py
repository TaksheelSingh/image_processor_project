import cv2
from image_processor import ImageProcessor
from strategies.blur import BlurStrategy
from strategies.sharpen import SharpenStrategy
from strategies.edge_detection import EdgeDetectionStrategy

# Load image
image_path = "sample.jpg"
image = cv2.imread(image_path)

# Initialize processor
processor = ImageProcessor(BlurStrategy())

while True:
    print("\nSelect an Image Processing Technique:")
    print("1. Blur")
    print("2. Sharpen")
    print("3. Edge Detection")
    print("4. Exit")

    choice = input("Enter choice: ")
    
    if choice == "1":
        processor.set_strategy(BlurStrategy())
    elif choice == "2":
        processor.set_strategy(SharpenStrategy())
    elif choice == "3":
        processor.set_strategy(EdgeDetectionStrategy())
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again.")
        continue

    # Process and show image
    processed_image = processor.process(image)
    cv2.imshow("Processed Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
