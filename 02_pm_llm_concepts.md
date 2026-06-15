# PM Concepts for LLMs

In software development, we go from Idea to Code. In AI development, we go from **Prompt** to **Inference**. As a PM, you need to manage the artifacts that control this process.

### The "System Prompt"
This is the "Configuration" of the AI. It is the instruction given to the model *before* the user interacts with it.
* *Example:* "You are a helpful Senior Python Developer. You answer concisely."
* *PM Relevance:* This is where you define the product's persona and constraints.

### Context Window
The "Short-term memory" of the model. 
* If you feed the model a 50-page PDF, and it forgets the first page, you have exceeded the context window.
* *Local LLM constraint:* Local models often have smaller context windows than for example OpenAI's GPT-4.

### Latency vs. Throughput
* **Latency:** Time to first token (how long the user waits before text appears).
* **Throughput:** Tokens per second (how fast the text types out).
* *PM Relevance:* Local models on a laptop usually have high latency. You need to decide if this UX is acceptable for your use case.

### Temperature
A hyperparameter that controls randomness.
* **0.0:** Fact-based, rigid, repetitive.
* **1.0:** Creative, hallucination-prone.
* *PM Requirement:* You must define the temperature in your spec sheet based on the feature type (Creative writing vs. Data classification).

### JSON Mode
Forcing the model to output structured data (JSON) instead of free text.
* *PM Relevance:* Essential for integrating AI into software pipelines reliably.