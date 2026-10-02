# Simple RAG Application with LangChain, FAISS and Groq

A beginner-friendly Retrieval-Augmented Generation (RAG) application built with Python, LangChain, Hugging Face embeddings, FAISS and Groq.

This project demonstrates the basic RAG pipeline:

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Retrieved Context
      ↓
Groq LLM
      ↓
Grounded Answer
```

The purpose of this project is to help learners understand the fundamental building blocks of a RAG application before moving to more advanced frameworks and production architectures.

---

## 1. What This Application Does

The application contains a small set of insurance and banking-related information.

For example:

- Customers can cancel their insurance policy within 14 days of purchase.
- Customers should contact the bank immediately if their banking credentials are exposed.
- The bank may temporarily hold a suspicious transaction while verification is completed.
- Complaints can be raised through customer support, online banking, or a branch.
- The bank aims to provide a final response to standard complaints within 15 business days.

The application converts this information into embeddings, stores those embeddings in a FAISS vector store, retrieves relevant chunks for each user question, and sends only the retrieved context to the Groq LLM.

---

# 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12.x | Programming language |
| VS Code | Development environment |
| LangChain | RAG orchestration |
| Hugging Face | Embedding model |
| Sentence Transformers | Generates embeddings |
| FAISS | Local vector store |
| Groq | LLM inference |
| python-dotenv | Environment variable management |

---

# 3. Prerequisites

Before starting, install:

1. Git
2. Python 3.12.x
3. Visual Studio Code
4. VS Code Python extension
5. A Groq account
6. A Groq API key

You do not need:

- Anaconda
- Docker
- Kubernetes
- A database server
- A cloud account
- A GPU

This project uses FAISS locally and a hosted Groq LLM.

---

# 4. Install Git

## Windows

Download Git from:

https://git-scm.com/downloads

After installation, open PowerShell or Git Bash and verify:

```bash
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

## macOS

If Git is already installed:

```bash
git --version
```

If macOS asks you to install Command Line Tools, accept the installation.

---

# 5. Install Python 3.12

Python 3.12.x is recommended for this project.

Python 3.12.5 is the version used while developing/testing this training material.

Download Python from the official Python website:

https://www.python.org/downloads/

Python 3.12.5:
https://www.python.org/downloads/release/python-3125/

---

## Windows Installation

Download the Windows installer.

During installation:

### IMPORTANT

Enable:

```text
Add python.exe to PATH
```

Then select:

```text
Install Now
```

After installation, open a **new** PowerShell window.

Verify:

```powershell
python --version
```

Expected:

```text
Python 3.12.x
```

Also verify pip:

```powershell
python -m pip --version
```

If `python` is not recognized, try:

```powershell
py --version
```

If `py` works but `python` does not, Python may not have been added to PATH.

---

## macOS Installation

Install Python 3.12 from the official Python website.

Open Terminal and verify:

```bash
python3 --version
```

Expected:

```text
Python 3.12.x
```

Verify pip:

```bash
python3 -m pip --version
```

> Note: macOS commonly uses `python3` instead of `python`.

---

# 6. Install Visual Studio Code

Download Visual Studio Code:

https://code.visualstudio.com/

Install VS Code using the default installation options.

VS Code's Python setup requires three separate pieces:

1. VS Code
2. Python interpreter
3. Python extension

---

# 7. Install the Python Extension in VS Code

Open VS Code.

Go to:

```text
Extensions
```

Search for:

```text
Python
```

Install:

```text
Python
Publisher: Microsoft
```

The official VS Code Python documentation recommends installing VS Code, an actively supported Python interpreter, and the Microsoft Python extension. 

---

# 8. Clone the Repository

Open a terminal.

Navigate to the location where you want to store the project.

Example:

```bash
cd Documents
```

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Example:

```bash
git clone https://github.com/<username>/simple-rag.git
```

Move into the project:

```bash
cd simple-rag
```

---

# 9. Open the Project in VS Code

From the project directory:

```bash
code .
```

If the `code` command is not available, open VS Code manually and select:

```text
File → Open Folder
```

Select the `simple-rag` folder.

---

# 10. Create a Python Virtual Environment

A virtual environment keeps this project's Python packages isolated from other projects on your machine.

This is strongly recommended.

---

## Windows

Open the VS Code terminal.

PowerShell:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

at the beginning of your terminal prompt.

### If PowerShell blocks activation

You may see an execution-policy error.

Use:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

---

## macOS

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv)
```

at the beginning of the terminal prompt.

---

# 11. Select the Python Interpreter in VS Code

In VS Code:

```text
Ctrl + Shift + P
```

Windows/Linux

or:

```text
Cmd + Shift + P
```

macOS

Search for:

```text
Python: Select Interpreter
```

Select the interpreter inside:

```text
.venv
```

For example:

Windows:

```text
.venv\Scripts\python.exe
```

macOS:

```text
.venv/bin/python
```

This is an important step.

Make sure VS Code is using the `.venv` interpreter and not another Python installation.

---

# 12. Upgrade pip

With the virtual environment activated:

Windows:

```powershell
python -m pip install --upgrade pip
```

macOS:

```bash
python3 -m pip install --upgrade pip
```

If your virtual environment is active, you can normally use:

```bash
python -m pip install --upgrade pip
```

on both platforms.

---

# 13. Install Project Dependencies

Make sure you are inside the project directory.

Run:

```bash
pip install -r requirements.txt
```

This installs all required libraries.

The installation may take several minutes because the Hugging Face embedding stack downloads additional machine-learning dependencies.

---

# 14. Verify the Installation

Run:

```bash
pip list
```

You should see packages including:

```text
langchain-core
langchain-community
langchain-text-splitters
langchain-huggingface
langchain-groq
sentence-transformers
faiss-cpu
python-dotenv
```

You can also verify Python:

```bash
python --version
```

---

# 15. Create a Groq Account

The application uses Groq for LLM inference.

Go to:

https://console.groq.com/

Sign in or create a Groq account.

---

# 16. Create a Groq API Key

After signing into Groq Console:

1. Open the Groq Console.
2. Go to the API Keys section.
3. Create a new API key.
4. Give the key a meaningful name, for example:

```text
simple-rag-learning
```

5. Copy the generated API key.

### IMPORTANT

Treat your API key like a password.

Do NOT:

- Put it directly in Python code.
- Commit it to Git.
- Push it to GitHub.
- Share it in screenshots.
- Send it through chat/email.

---

# 17. Create the `.env` File

In the root of the project, create:

```text
.env
```

Add:

```text
GROQ_API_KEY=your_actual_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

For example:

```text
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
GROQ_MODEL=openai/gpt-oss-120b
```

Do not include quotes unless your key requires them.

---

# 18. Why We Use `.env`

The application contains:

```python
from dotenv import load_dotenv

load_dotenv()
```

This loads environment variables from `.env`.

The application then reads:

```python
os.getenv("GROQ_API_KEY")
```

and:

```python
os.getenv("GROQ_MODEL")
```

This keeps secrets and configuration outside the Python source code.

---

# 19. Verify `.gitignore`

Make sure your `.gitignore` contains:

```text
.env
.venv/
```

Run:

```bash
git status
```

You should NOT see `.env` listed as a file ready to commit.

---

# 20. Run the Application

Make sure the virtual environment is activated.

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

macOS:

```bash
source .venv/bin/activate
```

Then run:

```bash
python simple_rag.py
```

---

# 21. First Run

The application will create the embedding model.

The first execution may take longer because the Hugging Face model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

needs to be downloaded.

After that, you should see something similar to:

```text
Created 3 chunks.

Vector store created.
```

The exact number of chunks may vary if the source text or chunk configuration changes.

You will then see:

```text
Ask a question (or type 'exit'):
```

---

# 22. Try These Questions

Try:

```text
How long do customers have to cancel an insurance policy?
```

Expected answer should be based on the supplied information:

```text
Customers can cancel their insurance policy within 14 days of purchase.
```

Try:

```text
What should I do if my banking credentials are exposed?
```

Try:

```text
How can I raise a complaint?
```

Try:

```text
How long does the bank aim to take to respond to standard complaints?
```

Try a question that is not present:

```text
What is the interest rate for savings accounts?
```

The application should respond:

```text
I could not find that information.
```

This demonstrates the basic grounding behavior implemented in the prompt.

---

# 23. Exit the Application

Type:

```text
exit
```

and press Enter.

---

# 24. Understanding the RAG Pipeline

The application follows these steps.

### Step 1 — Source Data

The application starts with a piece of text:

```python
text = """
Customers can cancel their insurance policy within 14 days of purchase.
...
"""
```

---

### Step 2 — Create a Document

LangChain converts the text into a `Document`:

```python
document = Document(page_content=text)
```

---

### Step 3 — Chunking

The document is split into smaller pieces:

```python
RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)
```

Chunking makes it possible to retrieve smaller relevant pieces instead of sending the entire document to the LLM.

---

### Step 4 — Embeddings

The application uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to convert text into numerical vectors.

Conceptually:

```text
Text
 ↓
Embedding Model
 ↓
[0.12, -0.43, 0.78, ...]
```

---

### Step 5 — Vector Store

FAISS stores the vectors:

```python
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)
```

FAISS enables similarity-based retrieval.

---

### Step 6 — User Question

The user enters:

```text
How long can I cancel my insurance policy?
```

The question is also converted into an embedding.

---

### Step 7 — Similarity Search

The application searches FAISS:

```python
results = vectorstore.similarity_search(
    question,
    k=2
)
```

The two most relevant chunks are retrieved.

---

### Step 8 — Build Context

The retrieved chunks are combined:

```python
context = "\n".join(
    document.page_content
    for document in results
)
```

---

### Step 9 — Send Context to the LLM

The prompt instructs the LLM:

```text
Answer the question using ONLY the information provided below.
```

The retrieved context is included in the prompt.

---

### Step 10 — Generate Answer

Groq generates the final response.

The important concept is:

```text
LLM does not directly search the document.

Retriever finds relevant information.
       ↓
Relevant information is placed into the prompt.
       ↓
LLM generates the answer using that context.
```

This is the fundamental idea behind Retrieval-Augmented Generation.

---

# 25. Common Problems and Solutions

## Problem 1 — `python` command not found

### Windows

Try:

```powershell
py --version
```

If this works, Python is installed but may not be configured correctly in PATH.

Restart the terminal after installing Python.

---

### macOS

Try:

```bash
python3 --version
```

macOS commonly uses `python3`.

---

# Problem 2 — `pip` command not found

Instead of:

```bash
pip install -r requirements.txt
```

use:

```bash
python -m pip install -r requirements.txt
```

On macOS:

```bash
python3 -m pip install -r requirements.txt
```

---

# Problem 3 — VS Code uses the wrong Python interpreter

Use:

```text
Command Palette
→ Python: Select Interpreter
→ Select .venv
```

Then open a new terminal.

---

# Problem 4 — `GROQ_API_KEY` error

Make sure:

```text
.env
```

exists in the project root.

Example:

```text
simple-rag/
├── simple_rag.py
├── requirements.txt
├── .env
└── .gitignore
```

And `.env` contains:

```text
GROQ_API_KEY=your_actual_key
```

---

# Problem 5 — Groq model error

Groq periodically changes its available models.

Check the current model list in Groq Console:

https://console.groq.com/docs/models

Then update:

```text
GROQ_MODEL=...
```

in `.env`.

---

# Problem 6 — FAISS installation problem

First upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then:

```bash
pip install faiss-cpu
```

If that succeeds, run:

```bash
pip install -r requirements.txt
```

---

# Problem 7 — Hugging Face model download takes time

The first execution downloads:

```text
sentence-transformers/all-MiniLM-L6-v2
```

This is normal.

You need an internet connection during the first model download.

Subsequent runs can reuse the locally cached model.

---

# Problem 8 — SSL / corporate network issues

If you are working from a corporate machine, firewall/proxy restrictions may prevent:

- PyPI downloads
- Hugging Face model downloads
- Groq API calls

If this happens, check with your organization's network/security team rather than disabling security controls.

---

# 26. Project Files

```text
simple-rag/
│
├── simple_rag.py
│   └── Main RAG application
│
├── requirements.txt
│   └── Python dependencies
│
├── .env.example
│   └── Example environment configuration
│
├── .gitignore
│   └── Prevents secrets and local files from being committed
│
└── README.md
    └── Setup and usage instructions
```

---

# 27. Security Reminder

Never commit:

```text
.env
```

Never put:

```text
GROQ_API_KEY=...
```

inside:

```text
simple_rag.py
```

Never commit API keys to GitHub.

If an API key is accidentally committed, revoke/rotate it immediately.

---

# 28. Git Workflow for Learners

After making changes:

```bash
git status
```

Review the files.

Then:

```bash
git add .
```

Commit:

```bash
git commit -m "Add simple RAG application setup"
```

Push:

```bash
git push
```

Before pushing, verify that `.env` is not included:

```bash
git status
```

---

# 29. Expected Final Repository

Your repository should look approximately like:

```text
simple-rag/
│
├── simple_rag.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The following files should NOT be committed:

```text
.env
.venv/
__pycache__/
```

---

# 30. Learning Objectives

After completing this project, you should understand:

- What RAG means
- Why documents are chunked
- What embeddings are
- Why vector databases/vector stores are used
- How FAISS performs similarity search
- How retrieved context is passed to an LLM
- How LangChain connects the components
- How to use Hugging Face embedding models
- How to connect LangChain with Groq
- How to manage API keys using environment variables
- How to create a Python virtual environment
- How to run a Python project from VS Code

---

## Next Steps

Once this basic application is working, the natural progression is:

```text
Level 1
Simple RAG
    ↓
Level 2
RAG using PDF documents
    ↓
Level 3
Multiple documents
    ↓
Level 4
Metadata filtering
    ↓
Level 5
Conversation memory
    ↓
Level 6
RAG evaluation
    ↓
Level 7
RAG with production vector database
    ↓
Level 8
GraphRAG / Neo4j
    ↓
Level 9
Production RAG API
```

The goal is to understand each layer before introducing additional infrastructure.
