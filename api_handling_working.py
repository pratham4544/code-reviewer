import streamlit as st
import asyncio
import logging
from aiohttp import ClientSession
from aiolimiter import AsyncLimiter
from src.helper import ResponseLLM

# Configure rate limiting: 5 requests per minute
limiter = AsyncLimiter(2, 60)

# Configure basic logging
logging.basicConfig(level=logging.INFO)

async def fetch_gpt_response(user_question, file_name):
    try:
        # Apply rate limiting
        async with limiter:
            logging.info("Fetching GPT response for question: %s", user_question)
            llm = ResponseLLM()
            documents = llm.load_text(file_name)
            split_text = llm.split_text(documents)
            vector_store = llm.create_embeddings(split_text)
            response = llm.response(user_question=user_question, vector_store=vector_store)
            logging.info("Response received: %s", response)
            return response
    except Exception as e:
        logging.error("An error occurred: %s", e)
        st.error(f"An error occurred while fetching the GPT response: {e}")
        return None

async def handle_review_requests(user_question, uploaded_file):
    return await fetch_gpt_response(user_question, uploaded_file.name)

async def main_async():
    st.header('Code Reviewer')
    st.write('Upload your code files')

    uploaded_file = st.file_uploader("Choose a file", type=['py', 'java', 'js'])
    user_question = st.text_input('Additional Information')

    if st.button('Submit'):
        if uploaded_file is not None:
            with st.spinner('Processing...'):
                results = await handle_review_requests(user_question, uploaded_file)
                if results:
                    st.write(f'Review Summary: {results}')
                else:
                    st.write('Failed to fetch the review summary.')

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
