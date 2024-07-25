import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt import *
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_together.embeddings import TogetherEmbeddings





# Load environment variables
load_dotenv()



class ResponseLLM:
    def __init__(self, model=None, embeddings=None):
        # Initialize the model and embeddings, using defaults if none provided
        self.model = model or ChatGroq(temperature=0.4, model="llama3-70b-8192", api_key=os.environ['GORQ_API_KEY'])
        self.embeddings = embeddings or TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval")

    def load_ebooks(self, ebooks):
        # Load documents from a directory of PDF files
        loader = PyPDFDirectoryLoader(ebooks)
        documents = loader.load()
        return documents


    def load_text(self, text):
        loader = TextLoader(text)
        documents = loader.load()
        return documents

    def split_text(self, documents):
        # Split documents into smaller chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        split_text = text_splitter.split_documents(documents)
        return split_text

    def create_embeddings(self, split_text):
        # Create embeddings for the text chunks and save them to a local FAISS index
        vector_store = FAISS.from_documents(split_text, embedding=self.embeddings)
        # vector_store.save_local("faiss_index")
        return vector_store
    

    def response(self, user_question, vector_store):
        # Generate a response to the user's question
        prompt_template = basic_prompt
        
        # Load the FAISS index based on the persona name
        # new_db = vector_store("faiss_index", self.embeddings, allow_dangerous_deserialization=True)
        # Perform a similarity search with the user's question
        docs = vector_store.similarity_search(user_question)
        # Create the prompt with context
        prompt = PromptTemplate(template=prompt_template, input_variables=["user_question", 'context'])
        print(prompt)
        # Chain the prompt with the model and output parser
        chain = prompt | self.model | StrOutputParser()
        # Generate the response
        response = chain.invoke({"context": docs, "user_question": user_question})
        
        
        return response
    
    
    def new_uploaded_file(self, text, user_question):
        documents = self.load_text(text)
        split_text = self.split_text(documents)
        vector_store = self.create_embeddings(split_text)
        response = self.response(user_question=user_question, vector_store=vector_store)
        
        return response

