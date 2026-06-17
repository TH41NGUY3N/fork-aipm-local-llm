import requests
import json
import sys
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"

# This script helps you understand how applications "talk" to AI models.
# You will implement a function to send a message to your local Ollama instance.

# Function to send a prompt to the local model
def query_ollama(model_name, prompt_text, timeout=30):
    """
    Args:
        model_name (str): The name of the local Ollama model (e.g., 'llama3.2:3b').
        prompt_text (str): The question or instruction for the AI.
        timeout (int): Seconds to wait before giving up.
        
    Returns:
        dict: A dictionary containing either the 'text' response or an 'error' message.
    """
    # The JSON payload required by the Ollama API contract
    payload = {
        "model": model_name,
        "prompt": prompt_text,
        "stream": False
    }

    try:
        # Send the POST request to the local server
        response = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
        response.raise_for_status() # Raises an error for bad HTTP status codes (like 404 or 500)
        
        # Parse the JSON response
        response_json = response.json()
        
        # Common keys for textual output in Ollama
        response_text = response_json.get("response", "")
        
        # Return a structured dictionary
        return {"text": response_text, "error": None}
        
    except Exception as e:
        # If anything goes wrong, return the error gracefully
        return {"text": None, "error": str(e)}

# Function to save the result to a file (for documentation)
def save_output_to_file(filename, content):
    """Saves the generated text to a local file using pathlib."""
    file_path = Path(filename)
    file_path.write_text(content, encoding="utf-8")
    return True

# Main execution block
if __name__ == "__main__":

    print("Initializing Local AI Connection...")

    # Define our inputs
    my_model = "llama3.2:3b"
    my_prompt = "Explain Agile methodology in one sentence."

    # Call our function
    result = query_ollama(my_model, my_prompt)

    # Check for errors before trying to print or save
    if result.get("error"):
        print(f"An error occurred: {result['error']}")
        sys.exit(1) # Exit the script with an error code

    # Extract the successful text
    response_text = result.get("text")
    print(f"\n🤖 AI Response:\n{response_text}\n")

    # Save it to a file
    saved = save_output_to_file("ollama_output.txt", response_text)
    if saved:
        print("✅ Result successfully saved to 'ollama_output.txt'")