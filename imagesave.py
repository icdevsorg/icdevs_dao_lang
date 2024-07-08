import os
from PIL import Image

def convert_pngs_in_directory(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG
        if filename.lower().endswith('.png'):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            
            try:
                # Open the image file
                with Image.open(file_path) as img:
                    # Perform any operations on the image here if needed
                    
                    # Save the image back to the same directory
                    img.save(file_path)
                    print(f"Processed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
directory_path = 'content/patterns/output/illustrations'
convert_pngs_in_directory(directory_path)
