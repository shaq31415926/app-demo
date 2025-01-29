import streamlit as st
import time


def welcome():
    placeholder = st.empty()
    # place a progress bar
    placeholder.progress(0, "IT HAS BEEN A PLEASURE TEACHING Y'ALL!")
    time.sleep(2.5)
    placeholder.progress(50, "THANK YOU 😍")
    time.sleep(2.5)
    placeholder.progress(100, "IF YOU WOULD LIKE SOME PARTING WORDS OF WISDOM, ENTER THE APP")
    time.sleep(0.75)
