# simple_rag.py

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# --------------------------------------------------
# 1. SOURCE DATA
# --------------------------------------------------

text = """
Customers can cancel their insurance policy within 14 days of purchase.
Customers should contact the bank immediately if their banking credentials are exposed.
The bank may temporarily hold a suspicious transaction while verification is completed.
Complaints can be raised through customer support, online banking, or a branch.
The bank aims to provide a final response to standard complaints within 15 business days.
"""

# --------------------------------------------------
# 2. CREATE DOCUMENT
# --------------------------------------------------

document = Document(page_content=text)

# --------------------------------------------------
# 3. SPLIT DOCUMENT INTO CHUNKS
# --------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_documents([document])

print(f"\nCreated {len(chunks)} chunks.")

# --------------------------------------------------
# 4. CREATE EMBEDDINGS
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --------------------------------------------------
# 5. STORE EMBEDDINGS IN VECTOR STORE
# --------------------------------------------------

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

print("Vector store created.")

# --------------------------------------------------
# 6. CREATE LLM
# --------------------------------------------------

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
    temperature=0
)

# --------------------------------------------------
# 7. ASK QUESTIONS
# --------------------------------------------------

while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    results = vectorstore.similarity_search(
        question,
        k=2
    )

    context = "\n".join(
        document.page_content
        for document in results
    )

    # --------------------------------------------------
    # 8. SEND QUESTION + RETRIEVED CONTEXT TO LLM
    # --------------------------------------------------

    prompt = f"""
Answer the question using ONLY the information provided below.

If the answer is not present in the information,
say: "I could not find that information."

Information:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)
