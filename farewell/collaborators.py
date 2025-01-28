import streamlit as st


def collaborators():
    with st.chat_message("user"):
        st.subheader("Open call!")
        c1, c2 = st.columns(2)
        with c1:
            text = """As some of you may already know, I’m planning to start my own company. One of my main goals is to create opportunities and provide experience to those who may not have access to it. I’m currently in the ideation stage, so there’s no funding YET, but the idea is COOL, if I do say so myself. 
                    I would be fully transparent about the company’s financial situation with founding members.
                    Right now, I’m developing the app and looking for collaborators to help launch it. It’s a low-commitment, low-risk opportunity, and I’m sharing this by the off chance it might align with your future goals — for example, be the HEAD OF MARKETING for my startup. We could really create any role, provided it helps get the company off the ground!
                    I don’t want to exploit anyone’s time or resources, but this is a great chance to experiment, make mistakes, and learn. I’m keeping things brief on purpose because I’m looking for someone who’ll say, ‘Hell yeah! I want in!’
                    If this resonates with you, drop me an email. Otherwise, feel free to follow me on LinkedIn and stay tuned for my exciting journey! :)
                   """
            st.write(f'<p style="font-size: 11.5px; color:grey; text-align: justify;">{text}</p>',
                     unsafe_allow_html=True)

        with c2:
            # add a giphy, even though slightly truncation
            gif_link = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnZ3cmN6bnpwM281dDRpaDVnMnp6MnRxendiZTR2dGk0Nnp3NDFzdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LoCDk7fecj2dwCtSB3/giphy.gif"
            st.markdown(
                f"<img src='{gif_link}' width='300'>",
                unsafe_allow_html=True
            )
