import streamlit as st

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
    st.title("Welcome to SOL")

    with st.chat_message("user"):
        st.write("Are you interested in:")
        buying = st.button("1. Buying", on_click=track_buying)
        discovery = st.button("2. Learning more", on_click=activate_next_page)

if st.session_state.page_count == 1:
    with st.chat_message("user"):
        st.write("Do you have an artwork you would like to share?")
        image_file = st.file_uploader("Upload Your Image",
                                      type=["jpg", "png", "jpeg"])

        st.button("No - Help me!", on_click=activate_next_page)

if st.session_state.page_count == 2:
    with st.chat_message("user"):
        st.image("./images/image1.jpeg")
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 3:
    with st.chat_message("user"):
        st.image("./images/image1.jpeg")
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 4:
    with st.chat_message("user"):
        st.image("./images/image1.jpeg")
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 5:
    with st.chat_message("user"):
        st.image("./images/image1.jpeg")
        artwork_rating = st.select_slider("Rate this artwork",
                                          ['🤮', '😔', '😐', '😊', '😍'])

        st.button(f"Confirm you {artwork_rating} this artwork", on_click=activate_next_page)

if st.session_state.page_count == 6:
    with st.chat_message("user"):
        if st.session_state.buying:
            st.write("WE RECOMMEND YOU SHOULD BUY")
        else:
            st.write("WE THINK YOU WOULD LOVE")
        st.image("./images/image1.jpeg",
                 caption="Give us feedback")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.button("❤️", on_click=track_hearts)
        with c2:
            st.button("❌", on_click=activate_next_page)

if st.session_state.page_count == 7:
    with st.chat_message("user"):
        st.title("🚧")
        if st.session_state.hearts == 1:
            st.write("Thank you! We are glad you like your recs")
            st.button("Discover MORE ART")
        else:
            st.write("Thank you! Sorry our recs suck :( Would you like to take the quiz again?")
            st.button("Take Quiz Again")
