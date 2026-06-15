# Local LLM Integration Assignment

## Introduction
Today you are not just a Project Manager; you are an AI Engineer for the day. You will set up `llama3` (or `mistral`), a powerful open-source model, on your own laptop. 

Why does a PM need this?
1.  **Privacy:** You can test with sensitive data locally.
2.  **Cost:** It's free. No OpenAI credits required.
3.  **Understanding:** You will learn what "Latency" and "Tokens/second" actually *feel* like.

## Assignment
Focus on getting the pipeline working. Don't worry if the model hallucinates—we are testing the *infrastructure*, not the model intelligence.

### Step 1: The Terminal (CLI)
Before writing code, we must verify the engine is running.
1.  Open your terminal.
2.  Pull a small, efficient model. Type: `ollama pull llama3.2:1b`.
3.  Run the model interactively: `ollama run llama3.2:1b`.
4.  Ask it: "Explain Agile methodology in one sentence."
5.  **Success Criteria:** If it replies, your local server is active.

### Step 2: VS Code Integration
Project Managers often review code. Let's make VS Code smarter using your local model.
1.  Download the "Continue - open-source AI code agent" extension for VS Code.
2.  Open it (the icon is on the left side of VS Code).
3.  In the bottom click on the dropdown menu and select chat mode first.
4.  In the models dropdown menu click on add chat model, select Ollama as the provider and leave Autodetect on. Now press connect.
5.  You should be able to chat with the locally installed model now.

### Step 3: Python API Interaction
Now, let's automate it. We want to send a prompt to the model using Python, not the chat window. 
* Open `simple_llm_client.py`.
* Complete the function `query_ollama()`.
* You will need to send a `POST` request to `http://localhost:11434/api/generate`.
* The payload usually looks like: `{"model": "llama3", "prompt": "Why is documentation important?", "stream": False}`.

### Step 4: Parameter Tuning (Optional)
If you finish early, modify your function to accept a `temperature` argument. 
* Try `temperature: 0.0` (Deterministic, good for data extraction).
* Try `temperature: 0.9` (Creative, good for brainstorming).
* Observe the differences in the output.