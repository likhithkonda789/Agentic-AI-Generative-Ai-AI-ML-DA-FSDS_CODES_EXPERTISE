import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.title("Image Processing with OpenCV and Streamlit Created by Likhith")
   
    # Upload image
    uploaded_file = st.file_uploader(r'C:\Users\A3MAX SOFTWARE TECH\A VS CODE\11. CAPSTONE PROJECT_DEPLOYMENT\numpy matplotlib\ele1', type=["jpg", "jpeg", "png"])
   
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Convert to numpy array
        img_array = np.array(image)

        # Convert to grayscale using OpenCV
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        # Display grayscale image
        st.image(gray_image, caption='Grayscale Image', use_column_width=True, channels="GRAY")
      
        
           
        # Convert to numpy array
        img_array = np.array(image)

        # Convert to grayscale using OpenCV
        ycrcb_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2YCrCb)

        # Display grayscale image
        st.image(ycrcb_image, caption='YCrCbscale Image', use_column_width=True, channels="YCrCb")

if __name__ == "__main__":
    main()