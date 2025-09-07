import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the URL of the image you want to download: ").strip()

    # Create directory if not exists
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch image from URL
        response = requests.get(url, timeout=10)  # 10s timeout for practicality
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename is missing, generate one
        if not filename or '.' not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save the image
        filepath = os.path.join(save_dir, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully downloaded and saved as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

if _name_ == "_main_":
    fetch_image()