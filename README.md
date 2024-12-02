# Python Code Generator with CodeLlama

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)

A Streamlit-based web application that generates Python code from natural language descriptions using CodeLlama through Together AI.

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/YOUR_USERNAME/code-generator-streamlit)
[![Streamlit](https://img.shields.io/badge/Streamlit-View_App-red?logo=Streamlit)](https://YOUR_APP_URL.streamlit.app)

</div>

## 🚀 Overview

This application demonstrates the integration of Large Language Models (specifically CodeLlama) with a web interface to generate Python code based on user descriptions. Built with Streamlit and Together AI, it provides an intuitive interface for converting natural language requirements into functional Python code.

## ✨ Features

- 🤖 Natural Language to Code conversion using CodeLlama
- 🌐 Clean, user-friendly web interface built with Streamlit
- 🔒 Secure API key management
- ☁️ Cloud deployment ready
- 📝 Well-documented code generation
- 🛠️ Error handling and input validation

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/code-generator-streamlit
cd code-generator-streamlit
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create `requirements.txt`
```plaintext
streamlit
together
```

## 🔑 Configuration

1. Create `.streamlit/secrets.toml`:
```toml
TOGETHER_API_KEY = "your_together_api_key_here"
```

2. Run locally:
```bash
streamlit run app.py
```

## ☁️ Deployment

1. Push to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Deploy on Streamlit Cloud:
- Visit [Streamlit Cloud](https://streamlit.io/cloud)
- Connect your GitHub repository
- Set main file path: `app.py`
- Configure your Together AI API key in Streamlit Cloud secrets

## 💻 Usage

Here's a quick example of how to use the code generator:

### Input:
```plaintext
Create a function to reverse a string in Python
```

### Output:
```python
def reverse_string(text):
    """
    Reverse a given string.
    
    Parameters:
    text (str): The string to be reversed
    
    Returns:
    str: The reversed string
    """
    return text[::-1]

# Example usage
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)  # Output: "!dlroW ,olleH"
```

## 📁 Project Structure

```
code-generator-streamlit/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .streamlit/           # Streamlit configuration
│   └── secrets.toml      # API keys and secrets
└── README.md             # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes. All rights reserved.

## 🙏 Acknowledgments

- Based on tutorial by Dr. Ernesto Lee
- Together AI for providing the CodeLlama model
- Streamlit for the web framework

---

<div align="center">
Created with ❤️ by [YOUR_NAME]
</div>
