import os

from langchain.chat_models import init_chat_model

# Set your key in the environment instead of writing it in code:
#   export GROQ_API_KEY="your-key"        (Linux / macOS)
#   setx GROQ_API_KEY "your-key"          (Windows)
# A local ApiKey.py (ignored by git) also works as a fallback.
if not os.environ.get("GROQ_API_KEY"):
    try:
        from ApiKey import ApiKey
        os.environ["GROQ_API_KEY"] = ApiKey
    except ImportError:
        raise SystemExit("GROQ_API_KEY is not set. See README.md.")

model = init_chat_model("llama3-8b-8192", model_provider="groq")
output = model.invoke("Hello! Introduce yourself in one sentence.")
print(output.content)
