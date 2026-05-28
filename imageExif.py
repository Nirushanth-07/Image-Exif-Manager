from exif import Image
import argparse
import os
from PIL import Image as img
from PIL import ImageOps
import sys
import random
import string

def get_file():
    parser = argparse.ArgumentParser(description="process image file path")
    parser.add_argument("file_path", help="The path to the image file")
    args = parser.parse_args()
    path = args.file_path
    
    if os.path.exists(path):
        print(f"Successfully recieved file: {path}\n")
        return path
    else:
        print(f"Error: The file {path} does not exist.")
        exit()

def extract_gps_decimal(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    decimal = degrees + minutes + seconds
    
    if ref in ['S', 'W']:
        decimal = -decimal
        
    return decimal

def show_exif(path):
    with open(path, "rb") as image_file:
        image = Image(image_file)

        if image.has_exif:
            print(f"--- EXIF data for {path} ---")
            for tag in image.list_all():
                try:
                    value = getattr(image, tag)
                    print(f"{tag.replace("_", " ").title()}: {value}")
                except:
                    pass
                
            if image.has_exif and "gps_longitude" in image.list_all():
                lat = extract_gps_decimal(image.gps_latitude, image.gps_latitude_ref)
                lon = extract_gps_decimal(image.gps_longitude, image.gps_longitude_ref)
                print(f"Latitude: {lat}, Longitude: {lon}  >>  {lat}, {lon}")
        else:
            print("No exif data to show.")
            exit()

def generate_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=15))

def update_exif(path):
    with open(path, "rb") as image_file:
        image = Image(image_file)

        if image.has_exif:
            print("If you want to keep the existing values, just press enter without typing.")
            for tag in image.list_all():
                try:
                    value = input(f"Enter the new value for {tag}: ")
                    if value:
                        setattr(image, tag, value)
                    sys.stdout.write("\033[F\033[K")
                    sys.stdout.flush()
                except:
                    pass
            sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()
        else:
            print("Image does not have exif data.")

        output = generate_random_string() + ".jpg"
        with open(output, "wb") as new:
            new.write(image.get_file())
        
        print(f"EXIF data updated. Saved to {output}")

def remove_exif(input_path):
    image = img.open(input_path)  
    image = ImageOps.exif_transpose(image)
    output = generate_random_string() + ".jpg"
    image.save(output, "JPEG", exif=b"", quality=100, subsampling=0, icc_profile=image.info.get("icc_profile"))

    print(f"All metadata stripped. Saved to {output}")


if __name__ == "__main__":
    path = get_file()
    show_exif(path)

    remove = input("\nDo you like to update (or remove) exif data? (0: remove all, 1: update): ")

    if remove == "0":
        remove_exif(path)
    elif remove == "1":
        update_exif(path)