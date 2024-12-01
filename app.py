import streamlit as st
import requests

# Set up the title and description
st.title("Together AI-Powered Python Code Generator")
st.write("Describe the Python code you'd like to generate, and this app will generate it for you using Together AI!")

# Input from user
description = st.text_area("Enter a description of the Python code:", "")

# Button to trigger code generation
if st.button("Generate Code"):
    if description.strip() == "":
        st.error("Please enter a description before clicking 'Generate Code.'")
    else:
        # Use Together AI's API
        api_url = "https://api.together.xyz/generate"
        api_key = st.secrets["TOGETHER_API_KEY"]
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"description": description}

        try:
            response = requests.post(api_url, json=payload, headers=headers)
            if response.status_code == 200:
                generated_code = response.json().get("code", "No code generated.")
                st.code(generated_code, language="python")
            else:
                st.error(f"Error: {response.status_code}. Unable to generate code.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
