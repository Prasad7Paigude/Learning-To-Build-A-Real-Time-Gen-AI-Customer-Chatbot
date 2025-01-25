# This file contains the code to generate a response using the Gemini model

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=[])
        
        response = chat.send_message(prompt, stream=True)

        response.resolve()
        
        if response and hasattr(response, 'text'):
            return " ".join(chunk.text for chunk in response)
        else:
            return "Error: Invalid response format from Gemini model."
    except Exception as e:
        return f"Error while using Gemini model: {str(e)}"

