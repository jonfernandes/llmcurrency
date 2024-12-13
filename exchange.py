import streamlit as st
import openai

import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

# Define the function to call the OpenAI API
def extract_currency_info(text):
    # Define the message to send to the API


    # Send the request to OpenAI API
    response = client.chat.completions.create(
        messages = [
        {
            "role": "system",
            "content": "You are an assistant who extracts currency exchange information from text."
        },
        {
            "role": "user",
            "content": text
        }
    ],
    model="gpt-4o",
    )

    # Extract the relevant information from the response
    try:
        currency_info = response.choices[0].message.content
        return currency_info
    except (KeyError, IndexError) as e:
        st.error(f"Error: {str(e)}")
        return None

# Streamlit app
st.title("Currency Converter")

# Text input for user
user_input = st.text_input("Enter currency conversion request:")

# Submit button
if st.button("Submit"):
    if user_input:
        # Use the OpenAI API to extract currency conversion information
        currency_info = extract_currency_info(user_input)
        
        # Display the extracted information
        if currency_info:
            st.write(currency_info)
    else:
        st.error("Please enter some text to extract currency information from.")