import os
from ApiKey import ApiKey
os.environ["GROQ_API_KEY"] = ApiKey
from langchain.chat_models import init_chat_model
model = init_chat_model("llama3-8b-8192", model_provider="groq")
output = model.invoke("")
print(output.content)