Image Processor Project

Overview

This project implements an Image Processing System using the Strategy Design Pattern. It allows users to apply different image processing techniques such as blurring, sharpening, and edge detection to images.

Features

✅ Apply different filters (Blur, Sharpen, Edge Detection) using interchangeable strategies✅ Modular and scalable design using the Strategy Pattern✅ Easy to extend by adding new processing strategies✅ Supports multiple image formats (JPG, PNG, etc.)

Technologies Used

Python 3.x

OpenCV (for image processing)

Pillow (PIL) (for image handling)

Installation

Clone this repository:

git clone https://github.com/TaksheelSingh/image_processor_project.git

Navigate to the project directory:

cd image_processor_project

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Usage

Place an image in the project directory (e.g., sample.jpg).

Run the program:

python main.py

The processed image will be saved in the output directory.

Example Output

Input: sample.jpg

Processing: Applying blur filter

Output: output/processed_sample.jpg

Adding New Strategies

To add a new image processing strategy:

Create a new file in strategies/ (e.g., new_filter.py).

Implement the apply method.

import cv2
import numpy as np
from strategy import ImageProcessingStrategy

class NewFilter(ImageProcessingStrategy):
    def apply(self, image):
        # Custom processing logic
        return image

Update main.py to include the new filter.

Contribution Guidelines

Fork the repository

Create a new branch (git checkout -b new-feature)

Commit changes (git commit -m "Added new feature")

Push to GitHub (git push origin new-feature)

Create a Pull Request

License

This project is licensed under the MIT License.

Developed by Taksheel Singh Rawat 🚀

