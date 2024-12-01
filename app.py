import streamlit as st
import requests

# Set up the app title and description
st.title("Together AI-Powered Python Code Generator")
st.write("Describe the Python code you'd like to generate, and this app will generate it for you using Together AI!")

# Input area for the user to describe the desired Python code
description = st.text_area("Enter a description of the Python code you'd like to generate:", "")

# Button to trigger code generation
if st.button("Generate Code"):
    # Ensure the user has entered a description
    if description.strip() == "":
        st.error("Please enter a description before clicking 'Generate Code.'")
    else:
        # Together AI API settings
        api_url = "https://api.together.xyz/generate"
        api_key = st.secrets["TOGETHER_API_KEY"]  # API key is securely stored in Streamlit Secrets
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"description": description}

        # Request to Together AI API
        try:
            response = requests.post(api_url, json=payload, headers=headers)
            
            # Handle the response
            if response.status_code == 200:
                generated_code = response.json().get("code", "No code was generated.")
                st.success("Code successfully generated! See below:")
                st.code(generated_code, language="python")
            else:
                st.error(f"Error {response.status_code}: Unable to generate code. Please try again.")
        
        # Handle connection or request errors
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while connecting to the Together AI API: {e}")
