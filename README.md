Ollama AI Model with Python
Introduction
This project is a simple Python application that communicates with the Ollama API to generate AI responses.
It allows users to enter a question and receive an answer from a locally running language model.
Features
Connect to the Ollama API.
Send prompts to an AI model.
Generate AI responses.
Receive responses in JSON format.
Check HTTP response status codes.
Run the AI model directly from the terminal.
Technologies
Python
Requests
JSON
Ollama
Gemma 3 1B
Project Structure
Ollama_Project/ ├── main.py ├── utils.py └── README.md 
Installation
Install the required Python library:
pip install requests 
Install Ollama and download the required model:
ollama pull gemma3:1b 
How to Run
Open the project in VS Code.
Make sure Ollama is installed and running.
Make sure the Gemma 3 1B model is available.
Run the Python file:
python utils.py 
Enter your question in the terminal.
The AI model generates a response.
How It Works
The application sends a POST request to the Ollama API.
The API receives the following parameters:
Prompt
Model name
Stream option
The response is received in JSON format and the generated text is extracted from the response.
API Endpoint
http://localhost:11434/api/generate 
AI Model
gemma3:1b 
The model generates responses based on the user's input.
Usage
The call_ollama_model() function accepts:
prompt: The user's question.
model: The name of the AI model.
stream: Determines whether the response is streamed.
The function returns the generated response as text.
Error Handling
The application checks the HTTP status code.
If the request fails, the function returns an error message.
Author
Python Programming Student
