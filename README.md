# LangChain + Groq Starter

A minimal starting point for building LLM apps with [LangChain](https://python.langchain.com/) and the [Groq](https://groq.com/) API (Llama 3 model).

## What it does

`TestDay1.py` creates a chat model with `init_chat_model("llama3-8b-8192", model_provider="groq")`, sends one prompt, and prints the reply.

## Setup

```bash
git clone https://github.com/ovibaridar/Langchain.git
cd Langchain
pip install langchain langchain-groq
```

Set your Groq API key as an environment variable (get one at https://console.groq.com):

```bash
# Linux / macOS
export GROQ_API_KEY="your-key"

# Windows (PowerShell)
$env:GROQ_API_KEY="your-key"
```

Run:

```bash
python TestDay1.py
```

> ⚠️ Never commit your API key. `ApiKey.py` and `.env` are listed in `.gitignore`.

## Tech

Python · LangChain · Groq · Llama 3
