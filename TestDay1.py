import os
from ApiKey import ApiKey
os.environ["GROQ_API_KEY"] = ApiKey
from langchain.chat_models import init_chat_model
model = init_chat_model("llama3-8b-8192", model_provider="groq")
output = model.invoke("give me a  model name which can find for me deep information using number or gmail or photos")
print(output.content)