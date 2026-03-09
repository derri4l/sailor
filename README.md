# rag
This project uses Python to create a RAG tool that parses notes. This was only intended for study purposes.

## How does it work
- First the program indexes your notes (.txt or .md).
- The notes gets chunked and turned into embeddings. During this process overlap is implemented so we don't loose context.
- Stores the vectors using FAISS.
- When we query now, the program retrieves the top 3 relevant chunks.
- Finally those top chunks get passed to an LLM to generate the final answer.

## Diagram
<img width="844" height="122" alt="Screenshot 2026-03-09 at 1 51 20 PM" src="https://github.com/user-attachments/assets/b95c431c-cc65-4ca8-8ee1-b95ec316bac6" />


## How to use

