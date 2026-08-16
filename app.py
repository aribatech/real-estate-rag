import streamlit as st
from dotenv import load_dotenv
from app.rag_chain import ask_question


load_dotenv()

# PAGE CONFIG
st.set_page_config(
    page_title="Real Estate AI",
    page_icon="🏠",
    layout="wide"
)


# HEADER
st.title("🏠 Real Estate AI")
st.caption("Ask questions about real estate properties.")


# CHAT
question = st.chat_input(
    "Ask about properties..."
)


if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            try:

                answer = ask_question(question)

                st.write(answer)

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )