import cv2
import numpy as np
import os

def make_bg_transparent(input_path, output_path):
    try:
        # Always read as 3-channel color image
        img_cv = cv2.imread(input_path, cv2.IMREAD_COLOR)
        if img_cv is None:
            print(f"Could not read {input_path}")
            return
            
        h, w = img_cv.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        
        # We assume background is at (0,0). Find the color at (0,0).
        # We flood fill from top-left (0,0) with magenta
        # Diff thresholds allow small compression artifacts to be included
        cv2.floodFill(img_cv, mask, (0,0), (255, 0, 255), (10, 10, 10), (10, 10, 10))
        
        # Convert to BGRA
        img_bgra = cv2.cvtColor(img_cv, cv2.COLOR_BGR2BGRA)
        
        b, g, r, a = cv2.split(img_bgra)
        
        # Where it is exactly magenta, set alpha to 0
        alpha = np.where((b == 255) & (g == 0) & (r == 255), 0, 255).astype(np.uint8)
        
        img_bgra[:,:,3] = alpha
        
        cv2.imwrite(output_path, img_bgra)
        print(f"Successfully processed {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

logos = [
    "images/husqvarna-logo.png",
    "images/pellenc-logo.png",
    "images/total-tools-logo.png",
    "images/ultra-scooter-logo.png",
    "images/big-boy-logo.png",
    "images/multi-power-logo.png"
]

for logo in logos:
    if os.path.exists(logo):
        make_bg_transparent(logo, logo)
    else:
        print(f"File not found: {logo}")
