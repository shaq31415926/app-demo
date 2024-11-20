import streamlit as st
import time
import requests

st.header("WELCOME TO MY JOKE APP")

button = st.button("Click here to laugh")
placeholder = st.empty()


def get_joke():
    # Reference: I asked chat gpt for a Joke API with minimal code
    # I then formatted it slightly, as it just happened to give me two part jokes

    url = "https://official-joke-api.appspot.com/random_joke"
    joke = requests.get(url).json()
    question = joke['setup']
    answer = joke['punchline']

    return question, answer


if button:
    question, answer = get_joke()
    placeholder.progress(0, "Wait for it")
    time.sleep(0.75)
    placeholder.progress(50, "Wait for it")
    time.sleep(0.75)
    placeholder.progress(100, "Wait for it")
    time.sleep(0.75)
    placeholder.write(question)
    time.sleep(3)
    placeholder.write(answer)
    time.sleep(2)
    https: // github.com / shaq31415926 / practical - experience - in -digital - media / blob / main / 05L
    ecture / images / snowman.jpeg?raw = true


    placeholder.audio("https://github.com/shaq31415926/app - demo/blob/main/mental-crisis-app/mixkit-drum-joke-accent-579.wav?raw = true", autoplay=True)
    time.sleep(2)
    placeholder.empty()
