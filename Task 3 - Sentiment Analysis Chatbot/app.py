import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model


# Loading the model
model = load_model('D:\\Desktop\\Internship\\Codes\\Customer Service Chatbot\\Tasks\\Task 3 - Sentiment Analysis\\Model training\\sentiment_analysis.h5')
vectorizer = pickle.load(open('D:\\Desktop\\Internship\\Codes\\Customer Service Chatbot\\Tasks\\Task 3 - Sentiment Analysis\\Model training\\tfidf_vectorizer.pkl', 'rb'))
responses_dict = pickle.load(open('D:\\Desktop\\Internship\\Codes\\Customer Service Chatbot\\Tasks\\Task 3 - Sentiment Analysis\\responses.pkl', 'rb'))

# Sentiment prediction function
def predict_sentiment(user_input):
    transformed_text = vectorizer.transform([user_input]).toarray()
    prediction = model.predict(transformed_text)
    sentiment_class = np.argmax(prediction)
    return sentiment_class

# Chatbot response function
def get_response(sentiment_class):
    if sentiment_class == 0:
        return np.random.choice(responses_dict['Negative'])
    elif sentiment_class == 1:
        return np.random.choice(responses_dict['Neutral'])
    else:
        return np.random.choice(responses_dict['Positive'])

# Streamlit app
st.title("Sentiment Analysis Chatbot 😊")
st.subheader("Chat with me and I'll predict the sentiment of your text!")

# User input
user_message = st.text_area("Enter your message here:")

if st.button("Send"):
    if user_message.strip() == "":
        st.error("Kindly enter a message.")
    else:
        # Prediction and Output
        sentiment = predict_sentiment(user_message)
        response = get_response(sentiment)

        # Displaying the Output
        st.markdown(f"👨‍🦰 **YOU**: {user_message}")
        st.markdown(f"🤖 **BOT**: {response}")