import cv2
import numpy as np

def fast_remove_bg(input_path, output_path):
    try:
        print("Using OpenCV")
        # Read as 3-channel BGR
        img_cv = cv2.imread(input_path, cv2.IMREAD_COLOR)
        
        h, w = img_cv.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        
        # flood fill from top-left (0,0) with magenta
        cv2.floodFill(img_cv, mask, (0,0), (255, 0, 255), (15, 15, 15), (15, 15, 15))
        
        # Convert to BGRA
        img_bgra = cv2.cvtColor(img_cv, cv2.COLOR_BGR2BGRA)
        
        # Make magenta transparent
        b, g, r, a = cv2.split(img_bgra)
        
        # Where it is exactly magenta
        alpha = np.where((b == 255) & (g == 0) & (r == 255), 0, 255).astype(np.uint8)
        
        img_bgra[:,:,3] = alpha
        
        # Write back
        cv2.imwrite(output_path, img_bgra)
        print("Successfully made background transparent with OpenCV.")
    except Exception as e:
        print(f"Error: {e}")

fast_remove_bg("images/logo.jpg", "images/logo.png")
