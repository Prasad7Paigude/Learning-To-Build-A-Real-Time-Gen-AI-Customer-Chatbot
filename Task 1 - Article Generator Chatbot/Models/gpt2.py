# This file contains the code to generate a response using the GPT-2 model

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def get_gpt2_response(prompt):
    try:
        model_name = "gpt2"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        
        tokenizer.pad_token = tokenizer.eos_token
        
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
        
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"], 
            max_length=200,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    except Exception as e:
        return f"Error while using GPT-2 model: {str(e)}"
