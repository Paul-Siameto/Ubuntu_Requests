import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt the user for the image URL
    url = input("Enter the image URL: https://unsplash.com/photos/tree-silhouetted-against-a-sunset-sky-viewed-from-cave-BnQForZBh-U ").strip()

    # Directory to store images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)  # Community & Sharing principle

    try:
        # Send request to fetch the image
        print("Connecting to the web community...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Path to save the image
        filepath = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Success! Image saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("⚠️ Error: Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. The server took too long to respond.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
