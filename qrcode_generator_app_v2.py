import streamlit as st
from generate_qrcode_page import generate_qrcode_page
from decode_qrcode_page import decode_qrcode_page

# code to config the page
st.set_page_config(
    page_title="QR Code Generator v2",
    page_icon="💫"
)

# creating a side menu bar
menu = ["QR Code Generator", "QR Code Decoder", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "QR Code Generator":
    st.subheader("QR Code Generator")
    generate_qrcode_page()
elif choice == "QR Code Decoder":
    st.subheader("QR Code Decoder")
    decode_qrcode_page()
elif choice == "About":
    st.subheader("About")
    #st.write("Hi! My name is Sarah and I :heart: Python")
    st.markdown(
        "<br><hr><center>Made with ❤️ by <a href='mailto:sarah.haq@leuphana.de?subject=QRCode Generator WebApp!&body=Please specify the issue you are facing with the app.'><strong>Sarah Haq</strong></a><br><br>Sarah is a Lecturer at Leuphana Uni and avid Pythonista.</center><hr>",
        unsafe_allow_html=True)
