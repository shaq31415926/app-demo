import streamlit as st
from welcome import welcome
from wisdom import wisdom
from collaborators import collaborators

# set up the page
st.set_page_config(page_title="FAREWELL",
                   page_icon="👋")

# app flag
if 'app_flag' not in st.session_state:
    st.session_state.app_flag = 0
# wisdom flag
if 'wisdom_flag' not in st.session_state:
    st.session_state.wisdom_flag = 0
# contact flag
if 'contact_flag' not in st.session_state:
    st.session_state.contact_flag = 0


def change_app_flag():
    st.session_state.app_flag = 1


def change_wisdom_flag():
    st.session_state.wisdom_flag = 1
    st.session_state.contact_flag = 0


def change_contact_flag():
    st.session_state.wisdom_flag = 0
    st.session_state.contact_flag = 1


# welcome the student and place button after progress bar loaded
if st.session_state.app_flag == 0:
    welcome()
    button = st.button("Click here",
                       on_click=change_app_flag)

# when the students click on button enter the app and give them options
if st.session_state.app_flag == 1:
    with st.chat_message("user"):
        st.write("Hello Student 👋")
        c1, c2 = st.columns(2)
        with c1:
            st.button("Click here for wisdom",
                      on_click=change_wisdom_flag,
                      use_container_width=True,
                      type="primary")

        with c2:
            st.button(
                "Interested in collaborating with me?",
                on_click=change_contact_flag,
                use_container_width=True,
                type="primary")

if st.session_state.wisdom_flag == 1:
    wisdom()

if st.session_state.contact_flag == 1:
    collaborators()


# markdown linking to email and code
if st.session_state.contact_flag == 1 or st.session_state.wisdom_flag == 1:
    st.markdown(
        "<br><hr><center><p style='font-size: 12px;'>Made with ❤️ by <a href='mailto:shaq@thecollectorsplatform.com?subject=I WANT TO COLLABORATE!'><strong>Sarah Haq</strong></a><br><br>You can find the code for the app <a href='https://github.com/shaq31415926/app-demo' target='_blank'><strong>here</strong></a>.</center><hr>",
        unsafe_allow_html=True)
