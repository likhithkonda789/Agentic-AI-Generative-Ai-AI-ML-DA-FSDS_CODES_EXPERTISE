import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="OpenCV  20 Colors images", layout="wide")
st.title("Upload Image → OpenCV 20 Colors images Output")

# ----------------------------
# Upload image
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "bmp"]
)

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    # Show original image
    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # ----------------------------
    # OpenCV Color Maps
    # ----------------------------
    color_maps = [
        cv2.COLORMAP_AUTUMN, cv2.COLORMAP_BONE, cv2.COLORMAP_JET,
        cv2.COLORMAP_WINTER, cv2.COLORMAP_RAINBOW, cv2.COLORMAP_OCEAN,
        cv2.COLORMAP_SUMMER, cv2.COLORMAP_SPRING, cv2.COLORMAP_COOL,
        cv2.COLORMAP_HSV, cv2.COLORMAP_PINK, cv2.COLORMAP_HOT,
        cv2.COLORMAP_PARULA, cv2.COLORMAP_MAGMA, cv2.COLORMAP_INFERNO,
        cv2.COLORMAP_PLASMA, cv2.COLORMAP_VIRIDIS, cv2.COLORMAP_CIVIDIS,
        cv2.COLORMAP_TWILIGHT, cv2.COLORMAP_TWILIGHT_SHIFTED
    ]

    # Apply color maps
    colored_images = []
    for cmap in color_maps:
        colored = cv2.applyColorMap(gray, cmap)
        colored = cv2.resize(colored, (300, 300))
        colored_images.append(colored)

    # Create grid (5x4)
    rows = []
    for i in range(0, 20, 5):
        row = cv2.hconcat(colored_images[i:i+5])
        rows.append(row)

    final_output = cv2.vconcat(rows)

    st.subheader("20 OpenCV Color Maps Output")
    st.image(final_output, channels="BGR", use_container_width=True)
