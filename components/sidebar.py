import streamlit as st


def sidebar():
    with st.sidebar:
        st.title("ℹ️ About")
        st.write("This website uses Mistral AI, to generate content for you instantly.")
        st.divider()
        st.markdown("**How to use:**")
        st.write("Choose a content type")
        st.write("Pick a tone")
        st.write("Enter your topic")
        st.write("Click Generate!")
        st.divider()
        st.caption("Built with Streamlit + Mistral AI")