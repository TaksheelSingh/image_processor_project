# Image Processor

This is an image processing project that applies various filters like **Blur**, **Sharpen**, **Edge Detection**, **Grayscale**, and **Contrast Enhancement** using the **Strategy Design Pattern**.

## Features
✅ Select an image from a dedicated `stored_images` folder
✅ Choose a processing technique
✅ Store the processed image in the `output` folder
✅ Supports multiple image formats: `.png`, `.jpg`, `.jpeg`
✅ Error handling for missing files or invalid input

## Folder Structure
```
image_processor_project/
│── strategies/               # Contains image processing strategies
│   ├── blur.py               # Blur effect
│   ├── sharpen.py            # Sharpening effect
│   ├── edge_detection.py      # Edge detection
│   ├── grayscale.py          # Grayscale conversion
│   ├── contrast.py           # Contrast enhancement
│── stored_images/            # Store images for processing
│── output/                   # Stores processed images
│── main.py                    # Main execution script
│── README.md                  # Project Documentation
```

## Installation & Usage
### 1️⃣ Install Dependencies
Ensure you have OpenCV installed:
```bash
pip install opencv-python
```

### 2️⃣ Add Images to `stored_images/`
Place the image you want to process inside the `stored_images/` folder.

### 3️⃣ Run the Program
```bash
python main.py
```

### 4️⃣ Select an Image & Processing Technique
- The script will display available images.
- Choose a processing method from:
  1️⃣ Blur
  2️⃣ Sharpen
  3️⃣ Edge Detection
  4️⃣ Grayscale
  5️⃣ Contrast Enhancement

### 5️⃣ Find the Processed Image
The processed image will be saved in the `output/` folder.

## Contribution
Feel free to contribute by improving the image processing strategies or adding new ones!

## License
📝 This project is open-source under the **MIT License**.
