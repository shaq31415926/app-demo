import streamlit as st
from calculate_numbers import calculate_life_path_number, calculate_personality_number, calculate_soul_number, \
    calculate_destiny_number
from chatbot import generate_response

# set the page config info
st.set_page_config(
    page_title="Numerology App",
    page_icon="🔮")

# welcome message
st.title("Welcome to your very own Numerology Assistant")
st.markdown(
    "If you would like to learn more about numerology you can check this Spotify Podcast [here](https://open.spotify.com/episode/78w5hXBfHnzFTVHC3aQv3c).")

# set button counters
if 'lifepath_count' not in st.session_state:
    st.session_state.lifepath_count = 0

if 'personality_count' not in st.session_state:
    st.session_state.personality_count = 0

if 'soul_count' not in st.session_state:
    st.session_state.soul_count = 0

if 'destiny_count' not in st.session_state:
    st.session_state.destiny_count = 0


def activate_lifepath():
    st.session_state.lifepath_count = 1
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 0


def activate_personality():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 1
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 0


def activate_soul():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 1


def activate_destiny():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 1
    st.session_state.soul_count = 0


def display_prompt_result(prompt):
    with st.spinner("Thinking..."):
        response = generate_response(prompt)
        st.write(response)


with st.chat_message("assistant"):
    st.write("Hello Human👋! What would you like me to calculate?")
    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life Path Number",
                              on_click=activate_lifepath,
                              help="This number represents who you are at your core")
        personality_number = st.button("Personality Number",
                                       on_click=activate_personality,
                                       help="This is the mask you present to others"
                                       )
    with c2:
        destiny_number = st.button("Destiny Number",
                                   on_click=activate_destiny,
                                   help="This number unveils your life's purpose")
        soul_number = st.button("Soul Number",
                                on_click=activate_soul,
                                help="This number represents your inner most desires")

if st.session_state.lifepath_count == 1:
    with st.chat_message("assistant"):
        dob = st.date_input("When's your birthday", value=None)
        if dob:
            life_path_number = calculate_life_path_number(dob)
            st.write(f"Your Life Path is {life_path_number}")
            prompt_button1 = st.button(f"Would you like to learn more about your Life Path number {life_path_number}")
            if prompt_button1:
                prompt = f"Tell me about Life Path number {life_path_number}"
                display_prompt_result(prompt)

if st.session_state.personality_count == 1 or st.session_state.soul_count == 1 or st.session_state.destiny_count == 1:
    with st.chat_message("assistant"):
        name = st.text_input("What's your full name")
        if name:
            # st.write(f"Your full name is {name}")
            if st.session_state.personality_count == 1:
                personality_number = calculate_personality_number(name)
                st.write(f"Your Personality Number is {personality_number}")
                prompt_button2 = st.button(
                    f"Would you like to learn more about your Personality Number {personality_number}")
                if prompt_button2:
                    prompt = f"Tell me about Personality Number {personality_number}"
                    display_prompt_result(prompt)
            if st.session_state.soul_count == 1:
                soul_number = calculate_soul_number(name)
                st.write(f"Your Soul Number is {soul_number}")
                prompt_button3 = st.button(f"Would you like to learn more about your Soul Number {soul_number}")
                if prompt_button3:
                    prompt = f"Tell me about Soul Number {soul_number}"
                    display_prompt_result(prompt)
            if st.session_state.destiny_count == 1:
                destiny_number = calculate_destiny_number(name)
                st.write(f"Your Destiny Number is {destiny_number}")
                prompt_button4 = st.button(f"Would you like to learn more about your Destiny Number {destiny_number}")
                if prompt_button4:
                    prompt = f"Tell me about Destiny Number {destiny_number}"
                    display_prompt_result(prompt)