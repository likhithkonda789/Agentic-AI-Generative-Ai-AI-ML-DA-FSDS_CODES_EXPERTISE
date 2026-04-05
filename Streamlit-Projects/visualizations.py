import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.title("Image Processing with OpenCV and Streamlit")
    uploaded_file = st.file_uploader(
        "Choose an image", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", width="stretch")

        img_rgb = np.array(image)
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # Color spaces
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        bgra = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2BGRA)
        hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
        ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)

        # Thresholds (Black & White)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        adaptive = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        _, otsu = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # Split channels
        r, g, b = cv2.split(img_rgb)
        red_color = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
        green_color = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
        blue_color = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])

        # Convert color spaces back to RGB
        hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        lab_rgb = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        ycrcb_rgb = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)
        bgra_rgb = cv2.cvtColor(bgra, cv2.COLOR_BGRA2RGB)

        # Effects
        inverted = cv2.bitwise_not(img_rgb)
        enhanced = cv2.convertScaleAbs(img_rgb, alpha=1.4, beta=30)

        # Sepia
        sepia_kernel = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])
        sepia = cv2.transform(img_rgb, sepia_kernel)
        sepia = np.clip(sepia, 0, 255).astype(np.uint8)

        # Warm & Cool filters
        warm = img_rgb.copy()
        warm[:, :, 0] = np.clip(warm[:, :, 0] + 30, 0, 255)

        cool = img_rgb.copy()
        cool[:, :, 2] = np.clip(cool[:, :, 2] + 30, 0, 255)

        # Blur & edges
        blur = cv2.GaussianBlur(img_rgb, (11, 11), 0)
        median = cv2.medianBlur(img_rgb, 9)
        edges = cv2.Canny(gray, 100, 200)

        images = [
            img_rgb,
            cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB),
            bgra_rgb,
            hsv_rgb,
            lab_rgb,
            ycrcb_rgb,
            gray,
            binary,
            adaptive,
            otsu,
            r,
            g,
            b,
            red_color,
            green_color,
            blue_color,
            inverted,
            sepia,
            enhanced,
            warm,
            cool,
            cv2.applyColorMap(gray, cv2.COLORMAP_JET),
            cv2.applyColorMap(gray, cv2.COLORMAP_HOT),
            cv2.applyColorMap(gray, cv2.COLORMAP_OCEAN),
            cv2.applyColorMap(gray, cv2.COLORMAP_PLASMA),
            cv2.applyColorMap(gray, cv2.COLORMAP_TURBO),
            cv2.applyColorMap(gray, cv2.COLORMAP_SUMMER),
            cv2.applyColorMap(gray, cv2.COLORMAP_AUTUMN),
            cv2.applyColorMap(gray, cv2.COLORMAP_COOL),
            edges,
            blur,
            median
        ]

        titles = [
            "RGB", "BGR → RGB", "BGRA",
            "HSV → RGB", "LAB → RGB", "YCrCb → RGB",
            "Grayscale", "Binary (B/W)", "Adaptive Threshold", "OTSU Threshold",
            "Red Channel (Gray)", "Green Channel (Gray)", "Blue Channel (Gray)",
            "Red Channel (Color)", "Green Channel (Color)", "Blue Channel (Color)",
            "Inverted", "Sepia", "Enhanced",
            "Warm Filter", "Cool Filter",
            "JET", "HOT", "OCEAN", "PLASMA", "TURBO",
            "SUMMER", "AUTUMN", "COOL",
            "Canny Edge", "Gaussian Blur", "Median Blur"
        ]

        st.subheader("Image Outputs")

        cols = st.columns(4)
        for i, img in enumerate(images):
            with cols[i % 4]:
                st.image(img, caption=titles[i], width="stretch")

if __name__ == "__main__":
    main()
