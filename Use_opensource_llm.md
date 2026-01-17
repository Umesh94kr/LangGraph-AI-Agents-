Generate a HuggingFace token and create .env file to store it 

```
import os 
from dotenv import load_dotenv

load_dotenv()

# setup openai environment
hf_token = os.getenv('HF_TOKEN')
os.environ['HF_TOKEN'] = hf_token

```

We mostly used `llama3.2`  model 

1. Pull the Model
Before running the notebook, pull the model in your terminal:

In terminal run ```ollama pull llama3.2```

In notebook use this :
```
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    verbose=True
)
```