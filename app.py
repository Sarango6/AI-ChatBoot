import streamlit as st
from chatbot import chatbot_response


st.set_page_config(
    page_title="Alpha-AI Chatbot",
    page_icon="🤖"
)


st.title("🤖 Alpha-AI Chatbot")


if "messages" not in st.session_state:

    st.session_state.messages=[]



for msg in st.session_state.messages:

    st.chat_message(
        msg["role"]
    ).write(
        msg["content"]
    )



user_input = st.chat_input(
    "Ask something..."
)


if user_input:


    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )


    response = chatbot_response(
        user_input
    )


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )


    st.rerun()