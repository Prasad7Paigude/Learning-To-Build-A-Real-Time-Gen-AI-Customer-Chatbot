import pickle

responses = {
    "Positive" : ["Great!", "Amazing!", "That's great to hear!", "Awesome!", "I'm happy to hear that!", "Wonderful!"],
    "Neutral" : ["I see. What else can I help with?", "Okay.", "Got it.", "Understood.", "Alright.", "Thanks for sharing.", "Alright, let me know if I can assist further."],
    "Negative" : ["I'm sorry to hear that.", "That's unfortunate.", "I understand your frustration.", "I'm sorry.", "Let me help you with that."]
}

with open('responses.pkl', 'wb') as f:
    pickle.dump(responses, f)

print("Responses saved successfully!")