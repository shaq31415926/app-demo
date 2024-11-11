import segno
import streamlit as st
from datetime import datetime
import time
from PIL import Image


def generate_qrcode(url, dark_colour):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark=dark_colour).save("images/qrcode_streamlit.png")


def generate_qrcode_page():
    # place an image
    # you can either download an image, or include the image file path
    # st.image("images/main_banner.png")

    # place a title
    # st.title("THE QR CODE GENERATOR")

    # place a text input box
    url = st.text_input("Enter the data you would like to encode")

    dark_colour = st.color_picker("Pick a colour for the dark squares", "#8569a8")

    button = st.button("Click here to generate")

    # when the user clicks on the button and have entered a url
    if button and url:
        # create a spinner if you want to
        with st.spinner("Generate QR Code"):
            time.sleep(1.5)
        # generate a qr code
        generate_qrcode(url, dark_colour)
        # place the qr code
        st.image("images/qrcode_streamlit.png",
                 caption="My Generate QR Code")

    # warning for when user clicks on button without a url
    if button and url == "":
        st.warning("Please enter the data you would like to encode")
