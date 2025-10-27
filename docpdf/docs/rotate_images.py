#!/usr/bin/env python3
"""
Rotate transmitter images that need to be corrected
"""

import os
from PIL import Image

def rotate_image(input_path, output_path, degrees):
    """Rotate an image by the specified degrees"""
    try:
        img = Image.open(input_path)
        rotated = img.rotate(-degrees, expand=True)  # Negative for clockwise
        rotated.save(output_path, quality=95)
        print(f"✓ Rotated {os.path.basename(input_path)} by {degrees}° clockwise")
        return True
    except Exception as e:
        print(f"✗ Error rotating {input_path}: {e}")
        return False

def main():
    base_path = "/Users/nh1584/Documents/DroidCode/Kyber130/docs/images/transmitters"
    
    # Rotate transmitter_x7_external.jpg 90 degrees clockwise
    rotate_image(
        os.path.join(base_path, "transmitter_x7_external.jpg"),
        os.path.join(base_path, "transmitter_x7_external_rotated.jpg"),
        90
    )
    
    # Check other transmitter images
    print("\nChecking other transmitter images...")
    for img in ["transmitter_x7_example1.jpg", "transmitter_x7_example2.jpg", "transmitter_x7_example3.jpg"]:
        path = os.path.join(base_path, img)
        if os.path.exists(path):
            print(f"  - {img} exists")

if __name__ == "__main__":
    main()