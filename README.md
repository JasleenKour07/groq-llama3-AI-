# groq-llama3-AI

This project is an AI Tutor ChatBot named Genny, built with GROQ and llama3.

# Genny AI Chatbot
```markdown
Genny AI is an interactive chatbot designed to assist students with various computer science topics, including programming, databases, algorithms, operating systems, computer networks, data structures, and artificial intelligence.

## Features

- Interactive modules for different computer science topics
- Uses the Groq API for generating responses
- Easy to set up and run

## Requirements

- Python 3.6 or higher
- Groq Python package

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/genny-ai-chatbot.git
    cd genny-ai-chatbot
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install groq
    ```

4. Set up your Groq API key as an environment variable:
    - Create a file named `.env` in the root directory of the project.
    - Add your Groq API key to the `.env` file:
        ```plaintext
        GROQ_API_KEY=your_groq_api_key_here
        ```

## Usage

1. Run the chatbot:
    ```bash
    python genny_ai.py
    ```

2. Follow the prompts to select a module and start interacting with Genny AI.

## Code Overview

The main components of the chatbot are:

- **API Initialization**: The Groq client is initialized using the API key loaded from the environment variable.
- **Modules**: There are different modules for various computer science topics, each providing relevant assistance.
- **Main Function**: The main function provides a menu for users to select which module they want to explore.

## Troubleshooting

### Invalid API Key Error

If you encounter an error stating "Invalid API Key":

- Ensure that the API key in your `.env` file is correct and active.
- Contact Groq support if the issue persists.

### Invalid API Key Error (Directly use API Key in code)
- You can directly use the API Key in the code.
  ```api_key = 'your_groq_api_key_here'

try:
    # Initialize the Groq client with the API key
    client = Groq(api_key=api_key)
    print("Client initialized successfully.")
except Exception as e:
    print("Error initializing client:", e)
    client = None
    ```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

```




