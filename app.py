import streamlit as st
from mistralai import Mistral
from utils.api_handler import generate_content, handle_error
from components.sidebar import sidebar
from components.input_form import input_form
from components.output_section import output_section
from components.styles import apply_styles

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
apply_styles()

#SideBar
sidebar()

# title
st.title("✍️ AI Writing Assistent")
st.write("Fill in the details below and generate your content instantly.")
st.divider() # this will display horizondal line across page.
# input form
content_type, tone, topic, word_count = input_form()
       
#Button
# col1, col2, col3 = st.columns(3) # instead you can give like this,st.columns([5,1,1]). if you want different size for both columns
col1, col3 = st.columns(2)
with col1:
   generate_clicked = st.button("✨ Generate", use_container_width=True) # use_container_width=True means, it use the full width of the page for this button
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
if clear_clicked:
   st.session_state["output"] = ""
   st.rerun()
                        
# Output display
output_section()