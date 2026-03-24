import streamlit as st
from mistralai import Mistral
from utils.prompt_builder import build_prompt


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