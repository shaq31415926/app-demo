import streamlit as st
import numpy as np
import cv2

def decode_qrcode_page():
    image_file = st.file_uploader("Upload QR Code Image",
                                  type=["jpg", "png", "jpeg"])

    if image_file is not None:
        # annoying code to convert the uploaded qr code image into an image the decoder function can read
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # create a page with column structure
        c1, c2 = st.columns(2)

        with c1:
            # place the image on our app
            st.image(opencv_image,
                     caption="This is our QR Code",
                     width=200)
        with c2:
            # using a decoder function from cv2 to decode our qr codes
            detector = cv2.QRCodeDetector()
            decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
            st.write(f"The qr contains {decoded_info}")
            # st.write(point)
            # st.write(straight_qr)