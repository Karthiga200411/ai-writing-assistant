import streamlit as st


def output_section():
    if st.session_state["output"] != "":
        st.divider()
        #word count
        word_count_output = len(st.session_state["output"].split())
        col_title, col_count = st.columns([3,1])
        with col_title:
            st.success("Here is your generated content.")
        with col_count:
            st.metric("Words", word_count_output)   
        st.text_area("Output", value=st.session_state["output"], height=300, label_visibility="hidden")
        # word_count_output = len(st.session_state["output"])
        # st.caption(f"Word Count: {word_count_output} words.")
        # Download Button
        st.download_button(
        label="Download as .txt",
        data=st.session_state["output"],
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
        )