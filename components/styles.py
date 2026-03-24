import streamlit as st


def apply_styles():
        st.markdown("""
    <style>
                /* Main Background*/
                .stApp{
                backfround-color: #f8f9fa;
                }
                /* Title */
            h1 {
                color: #1a1a2e;
                font-family: Arial, sans-serif;
            }

            /* Buttons */
            .stButton > button {
                background-color: #1a1a2e;
                color: white;
                border-radius: 8px;
                border: none;
                padding: 10px;
                font-size: 16px;
            }

            .stButton > button:hover {
                background-color: #0f3460;
                color: white;
            }

            /* Text area */
            .stTextArea > div > div > textarea {
                background-color: #ffffff;
                border-radius: 8px;
                border: 1px solid #dddddd;
                font-size: 15px;
            }

            /* Divider */
            hr {
                border: 1px solid #e0e0e0;
            }

            /* Success box */
            .stSuccess {
                background-color: #e8f5e9;
                border-radius: 8px;
            }
                /* Fix cursor on selectbox */
    .stSelectbox > div > div {
        cursor: pointer;
                
                /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #e8eaf6;
    }

    /* Bold input labels */
    .stSelectbox label, .stRadio label, 
    .stTextArea label, .stSlider label {
        font-weight: bold;
        font-size: 16px;
        color: #1a1a2e;
    }
    }
                
        # this is for side bar highlighting begin
                /* Sidebar - minimal with border */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #1a1a2e;
    }

    /* Sidebar text color */
    [data-testid="stSidebar"] p {
        color: #1a1a2e;
    }

    /* Sidebar title */
    [data-testid="stSidebar"] h1 {
        color: #1a1a2e;
        font-size: 22px;
    }

    /* Sidebar caption */
    [data-testid="stSidebar"] small {
        color: #888888;
    }

    # this is for side bar highlighting ends

        </style>

    """, unsafe_allow_html=True) # unsafe_allow_html means, allow this css and html.