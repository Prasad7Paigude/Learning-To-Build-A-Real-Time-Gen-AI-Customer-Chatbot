# This file contains the code to generate a response using the Llama3 model

from langchain_ollama import OllamaLLM

def get_llama_response(prompt):
    try:
        llm = OllamaLLM(model="llama3")
        response = ""
        for token in llm.stream(input=prompt):
            response += token
        return response
    except Exception as e:
        return f"Error while using Llama3 model: {str(e)}"
