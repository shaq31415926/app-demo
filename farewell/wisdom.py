import streamlit as st


def wisdom():
    with st.chat_message("user"):
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("1. MEDITATE")
            st.video("https://www.youtube.com/watch?v=6c-opIl29F8")
        with c2:
            intro_text = """2. Feedback is a necessary for growth... """
            # if you want to adjust the size and colour of the font you have to use some html
            # update the font size and colour of your choice
            st.write(intro_text)

            intro_text = """
                   but it's crucial to distinguish between constructive and destructive feedback. Approach feedback with objectivity. Give it as a gift and receive it with an open mind but if you find yourself in a situation where the feedback stings, take a moment to process it and unpack it with someone you trust.
                   I’m still working through feedback I received 15 years ago because I internalised it 😔! And if I’ve ever been unkind in my feedback to you, please know it was never my intention—I’m genuinely sorry. 💛 YOU'RE AWESOME, and that's why getting feedback from testers is important so that you can get a holistic view of how your app works.
                   """
            # if you want to adjust the size and colour of the font you have to use some html
            # update the font size and colour of your choice
            st.write(f'<p style="font-size: 13px; color:grey; text-align: justify;">{intro_text}</p>',
                     unsafe_allow_html=True)