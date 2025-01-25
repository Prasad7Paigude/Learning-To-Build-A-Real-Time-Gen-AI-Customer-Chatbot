import streamlit as st
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

from Models.llama3 import get_llama_response
from Models.gemini import get_gemini_response
from Models.gpt2 import get_gpt2_response

st.set_page_config(page_title="Article Generator Chatbot 🤖")
st.title("Article Generator Chatbot 🤖")
st.sidebar.title("Select Model")


if "model_choice" not in st.session_state:
    st.session_state["model_choice"] = "Llama3"

model_choice = st.sidebar.selectbox(
    "Select a model:",
    options=["Llama3", "Gemini", "GPT-2"],
    index=["Llama3", "Gemini", "GPT-2"].index(st.session_state["model_choice"])
)

st.session_state["model_choice"] = model_choice

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

for msg in st.session_state["messages"]:
    if msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
    else:
        st.chat_message("user").write(msg["content"])

if model_choice:
    prompt = st.text_input("Message Chatbot", key="input")
    submit = st.button("SUBMIT")
    
    if submit and prompt:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        
        try:
            if model_choice == "Llama3":
                response = get_llama_response(prompt)
            elif model_choice == "Gemini":
                response = get_gemini_response(prompt)
            elif model_choice == "GPT-2":
                response = get_gpt2_response(prompt)
            else:
                response = "Invalid model choice"
        except Exception as e:
            response = [f"Error: {str(e)}"]

        if isinstance(response, str):
            response = [response]

        st.session_state["messages"].append({"role": "assistant", "content": response})

        for chunk in response:
            print(st.write(chunk))