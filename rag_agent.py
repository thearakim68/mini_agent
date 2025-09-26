import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangChain imports
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Load the text document
loader = TextLoader("documents/khmer_history.txt") # ✅ Load your knowledge base
documents = loader.load()

# Convert documents into vector embeddings
embeddings = OpenAIEmbeddings() # ✅ Uses OpenAI to create vector representations
vectorstore = Chroma.from_documents(documents, embeddings) # ✅ Store vectors in memory

# Turn vector store into a retriever
retriever = vectorstore.as_retriever()

# Load the chat model (GPT-4o)
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

# Combine the retriever + LLM into a QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm = llm,
    retriever = retriever,
)

# Ask the question
query = "What is the history of Cambodia?"
response = qa_chain.run(query)

# Print the result
print("📌 Your Question:", query)
print("🤖 Agent Answer:", response)