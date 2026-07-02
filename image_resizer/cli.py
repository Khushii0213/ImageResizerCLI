import argparse

from image_resizer.utils import get_image_files
from image_resizer.processor import resize_image


def run():
    """
    Main entry point for the CLI application.
    """

    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Batch Image Resizer"
    )

    # Input folder
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input folder containing images"
    )

    # Output folder
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the output folder"
    )

    # Resize width
    parser.add_argument(
        "--width",
        type=int,
        required=True,
        help="Width of the resized image"
    )

    # Resize height
    parser.add_argument(
        "--height",
        type=int,
        required=True,
        help="Height of the resized image"
    )

    # Read command line arguments
    args = parser.parse_args()

    # Find all images
    images = get_image_files(args.input)

    # Check if folder contains images
    if not images:
        print("❌ No supported image files found.")
        return

    print(f"\n📂 Found {len(images)} image(s):\n")

    # Resize every image
    for image in images:
        resize_image(
            image_path=image,
            output_folder=args.output,
            width=args.width,
            height=args.height
        )

    print("\n🎉 Batch resizing completed successfully!")