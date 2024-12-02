# 🚀 Python Code Generator with CodeLlama

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![Together AI](https://img.shields.io/badge/Together_AI-CodeLlama-orange)](https://www.together.ai/)
[![GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/cagBRT/code-generator-streamlit)

*This project closely follows the tutorial by [Dr. Ernesto Lee](https://drlee.io/building-a-python-code-generator-with-codellama-in-streamlit-cloud-4a78886918eb)*

---

<img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg" width="48" title="Python"> <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Git.svg" width="48" title="Git">

</div>

## 📖 Overview

A Streamlit web application that transforms natural language descriptions into Python code using CodeLlama's AI capabilities. Built with Streamlit Cloud and Together AI, this project makes code generation accessible through an intuitive interface.

### ✨ Key Features

- 🤖 AI-Powered Code Generation
- 🌐 User-Friendly Web Interface
- 🔒 Secure API Management
- ☁️ Cloud-Based Architecture
- 📝 Detailed Documentation Support

## 🎯 Quick Demo

![Code Generator Demo](https://raw.githubusercontent.com/cagBRT/code-generator-streamlit/main/demo.gif)

### Example Usage:

```python
Input: "Create a function to calculate the fibonacci sequence"

Output: 
def fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    :param n: The number of terms to generate
    :return: A list of the Fibonacci sequence up to the nth term
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence

# Example usage
fibonacci(5)  # returns [0, 1, 1, 2, 3]
```

## 🛠️ Setup & Deployment

1. **Clone & Install**
   ```bash
   git clone https://github.com/cagBRT/code-generator-streamlit
   cd code-generator-streamlit
   pip install -r requirements.txt
   ```

2. **Deploy & Configure**
   - Deploy via Streamlit Cloud
   - Configure Together AI API key
   - Full deployment instructions in the [original tutorial](https://drlee.io/building-a-python-code-generator-with-codellama-in-streamlit-cloud-4a78886918eb)

## 📚 Documentation

For detailed implementation steps and technical documentation, please refer to:
- [Original Tutorial by Dr. Ernesto Lee](https://drlee.io/building-a-python-code-generator-with-codellama-in-streamlit-cloud-4a78886918eb)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Together AI Documentation](https://docs.together.ai/)

## 📜 Attribution

This project is created for educational purposes, implementing the architecture and concepts presented in [Dr. Ernesto Lee's tutorial](https://drlee.io/building-a-python-code-generator-with-codellama-in-streamlit-cloud-4a78886918eb).

## 🙏 Acknowledgments

- Dr. Ernesto Lee is the author of the tutorial emulated here
- Together AI for providing the CodeLlama model
- Streamlit for the web framework
- The open-source community for continuous inspiration

---

<div align="center">

</div>
