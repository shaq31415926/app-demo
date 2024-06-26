import streamlit as st
from PIL import Image


if 'page_count' not in st.session_state:
    st.session_state.page_count = 0

if 'buying' not in st.session_state:
    st.session_state.buying = 0

if 'hearts' not in st.session_state:
    st.session_state.hearts = 0


def activate_next_page():
    st.session_state.page_count += 1


def track_buying():
    activate_next_page()
    st.session_state.buying = 1

def track_hearts():
    activate_next_page()
    st.session_state.hearts = 1


if st.session_state.page_count == 0:
    st.title("Welcome to SOAL")

    with st.chat_message("user"):
        st.write("Are you interested in:")
        buying = st.button("1. Buying", on_click=track_buying)
        discovery = st.button("2. Learning more", on_click=activate_next_page)

if st.session_state.page_count == 1:
    with st.chat_message("user"):
        st.write("Do you have an artwork you would like to share?")
        image_file = st.file_uploader("Upload as many images as you would like to",
                                      type=["jpg", "png", "jpeg"])

        st.button("No - Help me!", on_click=activate_next_page)

if st.session_state.page_count == 2:
    with st.chat_message("user"):
        image = Image.open("./images/image1.jpg")
        new_image = image.resize((400, 400))
        st.image(new_image)

        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])
        emotion_rating = st.select_slider("How does it make you feel?",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 3:
    with st.chat_message("user"):
        image = Image.open("./images/image2.jpg")
        new_image = image.resize((400, 400))
        st.image(new_image)
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])
        emotion_rating = st.select_slider("How does it make you feel?",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 4:
    with st.chat_message("user"):
        image = Image.open("./images/image3.jpg")
        new_image = image.resize((400, 400))
        st.image(new_image)

        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])
        emotion_rating = st.select_slider("How does it make you feel?",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 5:
    with st.chat_message("user"):
        image = Image.open("./images/image4.jpg")
        new_image = image.resize((400, 400))
        st.image(new_image)
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])
        emotion_rating = st.select_slider("How does it make you feel?",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

# TODO: If user likes all of them equally ask the user to rank
# TODO: If user dislikes all of them equally show more images or ask for more questions

if st.session_state.page_count == 6:
    with st.chat_message("user"):
        if st.session_state.buying:
            st.title("🚧 WE RECOMMEND YOU SHOULD BUY")
        else:
            st.title("🚧 WE THINK YOU WOULD LOVE")

        st.write("TELL US WHAT YOU THINK OF THE RECOMMENDATIONS")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.button("LOVE THEM - ❤️", on_click=track_hearts)
        with c2:
            st.button("HATE THEM - ❌", on_click=activate_next_page)

        st.image("./images/recs.PNG")



if st.session_state.page_count == 7:
    with st.chat_message("user"):
        st.title("🚧")
        if st.session_state.hearts == 1:
            st.write("Thank you! We are glad you like your recs")
            st.button("Discover MORE ART", on_click=activate_next_page)
        else:
            st.write("Thank you! Sorry our recs suck :( Would you like to take the quiz again?")
            st.button("Take Quiz Again", on_click=activate_next_page)

if st.session_state.page_count == 8:
    st.write("That's all for now. Refresh page to relaunch")