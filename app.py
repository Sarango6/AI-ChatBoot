import streamlit as st
from datetime import datetime

from chatbot import chatbot_response
from gemini_ai import ask_ai
from voice import voice_input


# Page settings
st.set_page_config(
    page_title="Alpha AI Assistant",
    page_icon="🤖"
)


# Sidebar
st.sidebar.title("🤖 Alpha AI")

st.sidebar.markdown(
"""
### Developer
Sarang Chavan
"""
)


# Initialize chat

if "messages" not in st.session_state:
    st.session_state.messages=[]


# Clear button

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages=[]

    st.rerun()



# Main UI

st.title("🤖 Alpha AI Assistant")

st.write(
    "Your personal AI chatbot powered by OpenRouter"
)



# Voice Input


if st.button("🎤 Speak"):


    user_voice = voice_input()


    st.session_state.messages.append(

        {
            "role":"user",
            "content":user_voice,
            "time":datetime.now().strftime(
                "%I:%M %p"
            )
        }

    )

    with st.spinner("🤔 Thinking..."):
        response = ask_ai(user_voice)

        if response is None:
            response = chatbot_response(
                user_voice
            )

    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":response,
            "time":datetime.now().strftime(
                "%I:%M %p"
            )
        }

    )


    st.rerun()




# Display Chat


for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.write(
            msg["content"]
        )

        st.caption(
            "🕒 "+msg["time"]
        )




# Text Input


user_input = st.chat_input(
    "Ask anything..."
)



if user_input:


    st.session_state.messages.append(

        {
            "role":"user",
            "content":user_input,
            "time":datetime.now().strftime(
                "%I:%M %p"
            )
        }

    )

    with st.spinner("🤔 Thinking..."):
        response = ask_ai(
            user_input
        )

        # fallback old chatbot

        if response is None:

            response = chatbot_response(
                user_input
            )

    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":response,
            "time":datetime.now().strftime(
                "%I:%M %p"
            )
        }

    )


    st.rerun()