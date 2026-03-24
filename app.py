import streamlit as st
from mistralai import Mistral
from utils.prompt_builder import build_prompt

# st.title("AI Writing Assistent")
# st.write("Welcome! this app will help you to generate content.")

# ── Initialize session state ──
if "output" not in st.session_state:
    st.session_state["output"] = ""

# page config (it must be the first command in streamlit app)
st.set_page_config( # it will show in the header tab in the page
    page_title=("AI Writing Assistent"),
    page_icon="✍️",
    layout="wide", # instead of centered give wide also
    initial_sidebar_state="expanded"
)
#CSS

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

#SideBar
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

# ── Header ──
# st.markdown("""
#     <div style="text-align: center; padding: 20px 0px;">
#         <h1>✍️ AI Writing Assistant</h1>
#         <p style="color: #666666; font-size: 18px;">
#             Fill in the details below and generate your content instantly.
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# title
st.title("✍️ AI Writing Assistent")
st.write("Fill in the details below and generate your content instantly.")
st.divider() # this will display horizondal line across page.
# input form
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

# Helper function to call the API
def generate_content(content_type, tone, topic, word_count):
   prompt = build_prompt(content_type, tone, topic, word_count) 
   client = Mistral(
               api_key = st.secrets["MISTRAL_API_KEY"]
            )
   response = client.chat.complete(
               model="mistral-small-latest",
               max_tokens=1000,
               messages=[
                  {
                     "role":"user",
                     "content": prompt
                  }
               ]
            )
   return response.choices[0].message.content
# Handle error
def handle_error(e):
   error = str(e)
   if "401" in error or "invalid_api_key" in error:
      st.error("Invalid API Key. Please Check your secrets.toml file.")
   elif "429" in error or "rate_limit" in error:
      st.error("Too many Requests. Please wait a moment and try again.")
   elif "500" in error or "server_error" in error:
      st.error("Mistral service is temporarily available. Try again later.")
   elif "network" in error.lower() or "connection" in error.lower():
      st.error("No internet connection . Please Check your Network.")  
   else:
      st.error(f"Something went wrong: {e}")          
#Button
# col1, col2, col3 = st.columns(3) # instead you can give like this,st.columns([5,1]). if you want different size for both columns
col1, col3 = st.columns(2)
with col1:
   generate_clicked = st.button("✨ Generate", use_container_width=True) # use_container_width=True means, it use the full width of the page for this button
# with col2:
#    regenerate_clicked  = st.button("🔄 Regenerate", use_container_width=True) 
with col3:
   clear_clicked = st.button("🗑️ Clear", use_container_width=True)   
#Generate Logic
if generate_clicked:
   if not topic.strip(): # strip => just remove the empty space, and check whether it is empty or not.
      st.warning("Please Enter a topic before Generating.")
   elif len(topic)>500:
      st.warning("Topic is too long. Please keep it under 500 character.")    
   else:
      #show a spinner while waiting for API
      with st.spinner("Generating your Content..."):
         try:
            output = generate_content(content_type, tone, topic, word_count)
            if not output.strip():
               st.warning("AI returned empty resposne. Please try again.")
            else:   
               st.session_state["output"] = output
         except Exception as e:
            handle_error(e)
# Regeneration Logic
# if regenerate_clicked:
#    if st.session_state["output"] == "":
#       st.warning("⚠️ Please generate content first before regenerating.")
#    elif not topic.strip():
#       st.warning("⚠️ Please Enter a topic before Generating.")
#    elif len(topic)>500:
#       st.warning("Topic is too long. Please keep it under 500 character.")   
#    else:
#       #show a spinner while waiting for API
#       with st.spinner("Regenerating..."):
#          try:
#             output = generate_content(content_type, tone, topic, word_count)
#             if not output.strip():
#                st.warning("AI returned empty resposne. Please try again.")
#             else:   
#                st.session_state["output"] = output
#          except Exception as e:
#             handle_error(e) 
if clear_clicked:
   st.session_state["output"] = ""
   st.rerun()
                        
# Output display
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