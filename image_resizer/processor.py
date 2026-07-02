from pathlib import Path
from PIL import Image


def resize_image(image_path, output_folder, width, height):
    """
    Resize a single image and save it to the output folder.
    """

    # Open the image
    img = Image.open(image_path)

    # Resize the image
    resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

    # Create output folder if it doesn't exist
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # Save the resized image
    output_file = output_path / image_path.name
    resized_img.save(output_file)

    print(f"✅ Resized: {image_path.name}")