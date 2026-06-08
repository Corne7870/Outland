from PIL import Image

def remove_white_bg(input_path, output_path, threshold=220):
    try:
        img = Image.open(input_path).convert("RGBA")
        data = img.getdata()

        new_data = []
        for item in data:
            # Check if pixel is close to white
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                new_data.append((255, 255, 255, 0)) # Fully transparent
            else:
                new_data.append(item) # Keep original pixel

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print("Successfully made background transparent.")
    except Exception as e:
        print(f"Error: {e}")

remove_white_bg("images/logo.jpg", "images/logo.png")
