import sys
import os
import openai
import numpy as np
import faiss
from dotenv import load_dotenv

#load OpenAi api key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

knowledge_dir = "../knowledge/"

# List all txt notes in knowledge
def list_notes(folder=knowledge_dir):
    files = [f for f in os.listdir(folder) if f.endswith((".txt"))]
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    return files
# pick note
def select_note(files):
    choice = int(input("\nSelect a note(use numbers):")) -1
    return files[choice]
#read note
def load_note(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# split text into chunks w overlap
def chunk_text(text:str, chunk_size: int = 300, overlap: int = 80) -> list[str]:  #change based on note length
    if overlap >= chunk_size:
        raise ValueError('"Overlap must be smaller than the chunk"')
    words = text.split()
    chunks = []
    start = 0
    step = chunk_size - overlap
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += step
    return chunks

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    vectors = []
    for chunk in chunks:
        response = client.embeddings.create(
            model = "text-embedding-3-small",
            input = chunk
        )
        vectors.append(response.data[0].embedding)
    return vectors

# store returned vectors in FAISS index
def store_in_faiss(vectors: list[list[float]]):
    dimension = len(vectors[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors, dtype=np.float32))
    return index

def build_context(chunks: list[str]) -> str:
    return "\n\n".join(chunks)

# LLM prompt
def build_prompt(context: str, question: str) -> str:
    return f"""
    Only answer questions using the provided notes.

    Context:
    {context}

    Question:
    {question}
"""
def generate_answer(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    files = list_notes()
    selected = select_note(files)
    text = load_note(os.path.join(knowledge_dir, selected))
    chunks = chunk_text(text)
    print(f"Chunks: {len(chunks)}")
    print(f"chunk1: {chunks[0][:100]}")

