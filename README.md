<div align="center">

# 🖼️ Image Resizer CLI

**A lightweight Python command-line tool for fast and efficient batch image resizing.**

Resize hundreds of images in seconds using a simple CLI while maintaining a clean, modular codebase.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-0DB7ED?style=for-the-badge)](https://python-pillow.org)
[![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

Image Resizer CLI is a Python-based command-line application that automates batch image resizing.

Instead of manually opening and resizing images one by one, users can resize an entire folder with a single command.

This project demonstrates practical software engineering concepts including:

- Command Line Interface (CLI)
- Modular Python architecture
- Batch file processing
- Image manipulation using Pillow
- Error handling and logging
- Asynchronous programming using `asyncio`

---

## ✨ Features

- 📂 Batch image processing
- ⚡ Fast command-line interface
- 🖼️ Supports multiple image formats
- 📁 Automatic output folder creation
- 🛡️ Error handling and validation
- 🧩 Modular project structure
- 🚀 Lightweight and easy to use

---

## 📸 Demo

### Command

```bash
python main.py --input input --output output --width 800 --height 600
```

### Input

```
input/
├── photo1.jpg
├── photo2.png
├── photo3.jpeg
```

↓

### Output

```
output/
├── photo1.jpg
├── photo2.png
├── photo3.jpeg
```

All images are resized automatically.

---

## 📁 Project Structure

```text
ImageResizerCLI/
│
├── image_resizer/
│   ├── __init__.py
│   ├── resize.py
│   ├── utils.py
│   └── ...
│
├── input/
├── output/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ImageResizerCLI.git
```

Move into the project

```bash
cd ImageResizerCLI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

Resize all images inside the `input` directory.

```bash
python main.py \
    --input input \
    --output output \
    --width 800 \
    --height 600
```

### Parameters

| Argument | Description |
|----------|-------------|
| `--input` | Input image directory |
| `--output` | Output directory |
| `--width` | Target width |
| `--height` | Target height |

---

## 🛠️ Built With

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pillow | Image processing |
| argparse | CLI argument parsing |
| asyncio | Asynchronous execution |
| Logging | Error reporting |

---

## 🌍 Real-World Applications

- AI/ML dataset preprocessing
- Computer Vision pipelines
- Website image optimization
- Product catalog generation
- Mobile application assets
- Bulk image management

---

## 📈 Future Improvements

- [ ] Preserve aspect ratio
- [ ] Image compression
- [ ] PNG ↔ JPG conversion
- [ ] Recursive directory support
- [ ] Progress bar
- [ ] Image quality selection
- [ ] Metadata preservation
- [ ] AI dataset preprocessing mode
- [ ] Duplicate image detection

---





<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
