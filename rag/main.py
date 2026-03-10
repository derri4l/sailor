import sys
import os
import openai
import numpy as np
import faiss
from dotenv import load_dotenv

#load OpenAi api key
#load_dotenv()
#client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

knowledge_dir = "../knowledge/"

# List all txt notes in knowledge
def list_notes(folder=knowledge_dir):
    files = [f for f in os.listdir(folder) if f.endswith((".txt"))]
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    return files

if __name__ == "__main__":
    list_notes()
