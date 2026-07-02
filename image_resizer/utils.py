from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}


def get_image_files(input_folder):
    """
    Returns all supported image files from the input folder.
    """

    input_path = Path(input_folder)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Folder '{input_folder}' does not exist."
        )

    image_files = []

    for file in input_path.iterdir():

        if file.is_file():

            if file.suffix.lower() in SUPPORTED_EXTENSIONS:

                image_files.append(file)

    return image_files