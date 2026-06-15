# AI PM Coding Challenge - Local LLM Setup & Integration

Today we're going to demystify the "Black Box" of AI by setting up our own local Large Language Model (LLM) using Ollama. 

As an AI Project Manager, understanding how to run, query, and integrate models locally is crucial for understanding latency, privacy implications, and API structures without relying on cloud providers.

## Project Structure
```
AIPM-local-llm/
├── 01_assignment_guide.md/     # Start Here
├── 02_pm_llm_concepts.md/      # Theory 
├── 03_simple_llm_client.py/    # Task 1: Basic Python script
├── 04_Local_LLM_Metrics.ipynb/ # Task 2: Advanced Notebook for measuring
├── requirements.txt            # Final dependency list
└── README.md                   # You're here!
```
## Before you start

### Install Ollama from your terminal or their website

https://ollama.com/download

`macOS:`
```BASH
brew install ollama
```
`Windows:`
```BASH
choco install ollama
```
`Linux:`
```BASH
curl -fsSL https://ollama.com/install.sh | sh
systemctl start ollama
```

### Launch the Ollama client
```
ollama serve
```

```
ollama run llama3.2:3B
```

This step may take a couple minutes.  

To exit the Ollama client type `/bye`.

## Set up your Environment


### **`macOS`** type the following commands :

- Install the virtual environment and the required packages by following commands:

  ```BASH
  pyenv local 3.11.3
  python -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

  For `PowerShell` CLI :

  ```PowerShell
  pyenv local 3.11.3
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
  For `Git-Bash` CLI :

  ```BASH
  pyenv local 3.11.3
  python -m venv .venv
  source .venv/Scripts/activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

