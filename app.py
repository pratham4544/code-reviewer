import streamlit as st
from src.helper import ResponseLLM
import os


st.header('Code Reviewer')

st.write('Upload your code files')

uploaded_file = st.file_uploader("Choose a file", type=['py','java','js'])

user_question = st.text_input('Additional Information')

if st.button('Submit'):

    if uploaded_file is not None:
        file_name = uploaded_file.name
        llm = ResponseLLM()
        documents = llm.load_text(file_name)
        split_text = llm.split_text(documents)
        vector_store = llm.create_embeddings(split_text)
        response = llm.response(user_question=user_question, vector_store=vector_store)
        
        st.write(f'Review Summary: {response}')