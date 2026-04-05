import streamlit as st 
import numpy as np 
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Elephant Image Processor", layout="wide")

# Title
st.title("Elephant Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data 
def load_image():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
    headers = {"User-Agent": "Mozilla/5.0"}     # ✅ added

    response = requests.get(url, headers=headers)
    response.raise_for_status()                 # ✅ added

    if "image" not in response.headers.get("Content-Type", ""):
        raise ValueError("Response is not an image")   # ✅ added

    return Image.open(BytesIO(response.content)).convert("RGB")

# Load and display image
elephant = load_image()
st.image(elephant, caption="Original Elephant Image", use_container_width=True)

# Convert to NumPy array
elephant_np = np.array(elephant)
R, G, B = elephant_np[:, :, 0], elephant_np[:, :, 1], elephant_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(elephant_np)
green_img = np.zeros_like(elephant_np)
blue_img = np.zeros_like(elephant_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

elephant_gray = elephant.convert("L")
elephant_gray_np = np.array(elephant_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(elephant_gray_np, cmap=colormap)
ax.axis("off")

st.pyplot(fig)
