import streamlit as st


def input_form():
    content_type = st.selectbox(
        "What do you want to create?",
        ["Blog post intro", "LinkedIn Post", "Twitter/X thread opener", "Marketing Email", "Product Tagline"]
    )
    tone = st.radio(
        "Choose a tone:",
        ["Professional", "Casual & Friendly", "Persuasive", "Funny / Witty"],
    #  horizontal=True # we can remove this, if we want to show the button one by one.
    )
    topic = st.text_area(
        "What is your topic or idea?",
        placeholder="e.g A app for influencers.",
        height=120
    )
    st.caption(f"{len(topic.strip())}/500 characters.")
    word_count = st.slider(
        "Approximate Word Count",
        min_value=50,
        max_value=500,
        value=150,
        step=50,
        help="💡 50-100 for social posts, 150-300 for emails, 300-500 for blog intros."
    )
    st.divider()
    return content_type, tone, topic, word_count