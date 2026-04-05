import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import os

# Helper function to load image from a URL
def load_image_from_url(url):
    local_file = "elephant_real.jpg"   # ✅ NEW file name

    headers = {"User-Agent": "Mozilla/5.0"}

    # Download only once
    if not os.path.exists(local_file):
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(local_file, "wb") as f:
            f.write(response.content)

    return Image.open(local_file).convert("RGB")

# ✅ DIRECT & STABLE ELEPHANT IMAGE
elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"

# Load elephant image
elephant = load_image_from_url(elephant_url)

# Display original image
plt.figure(figsize=(6, 4))
plt.imshow(elephant)
plt.title("Elephant")
plt.axis("off")
plt.show()

# Convert to NumPy array and print shape
elephant_np = np.array(elephant)
print("Elephant image shape:", elephant_np.shape)

# Convert to grayscale
elephant_gray = elephant.convert("L")

# Display grayscale image
plt.figure(figsize=(6, 4))
plt.imshow(elephant_gray, cmap="gray")
plt.title("Elephant (Grayscale)")
plt.axis("off")
plt.show()
