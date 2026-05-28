# Image Exif Manager

A lightweight, powerful command-line interface (CLI) tool written in Python to manage image metadata. Whether you need to audit your photos for privacy, update copyright information, or simply view hidden camera settings, this tool provides a simple, robust interface.

## Features
* **View:** Extract and display all available EXIF tags.
* **Convert:** Automatically converts GPS DMS (Degrees/Minutes/Seconds) coordinates into standard decimal format.
* **Update:** Interactively modify metadata tags with validation.
* **Strip:** Securely remove all metadata to protect your privacy before sharing.
* **Orientation Fix:** Automatically transposes images based on orientation tags before stripping to prevent rotation issues.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nirushanth-07/Image-Exif-Manager.git
   ```
   ```bash
   cd Image-Exif-Manager
   ```
2. Create and activate a virtual environment:
   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script by providing the path to your image:
   ```bash
   python3 imageExif.py path/to/your/image.jpg
   ```
Follow the on-screen prompts to either remove all metadata or update specific EXIF tags interactively.

## Technical Dependencies
* Pillow: For high-quality image processing and orientation handling.
* exif: For deep, attribute-based manipulation of EXIF headers.

## License
Distributed under the MIT License. See LICENSE for more information.


**Would you like me to add a section for "Known Issues" or "Contributing" guidelines to this document?**