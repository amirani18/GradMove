# Building web application components
import streamlit as st

# Making HTTP requests
import requests

# Pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# Reading and manipulating PDF files
import PyPDF2

# Natural language processing tasks/building chatbot related
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI

# Make sidebar to insert OpenAI API key
openai_api_key = openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def main():
    # Insert title
    st.title("Research Assistant")
    # Insert file uploader
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    # Insert text input prompt
    prompt = st.text_input("Ask me anything about this research paper!")
    # Initialize history storage
    if st.session_state.get('history') is None:
        st.session_state.history = []
    # Scrape content from uploaded pdf file
    if uploaded_file is not None:
        pdf_text = pdf_scrape(uploaded_file)[:10000]
    # Set up prompt template
    question_template = PromptTemplate(
        input_variables = ['prompt', 'research'],
        template = 'While leveraging this research: {research}, answer this question: {prompt}'
    )
    # Use ConversationBufferMemory allows for storing messages and then extracts the messages in a variable
    title_memory = ConversationBufferMemory(input_key='prompt', memory_key='chat_history')
    # Build LLM Chain using LangChain
    # lower temp: more specific and predictable, higher is opposite
    llm = OpenAI(temperature=0.9, openai_api_key=openai_api_key)
    title_chain = LLMChain(llm=llm, prompt=question_template, verbose=True, output_key='title', memory=title_memory)
    # Run prompt through chain
    if prompt: 
        response = title_chain.run({'prompt': prompt, 'research': pdf_text})
        st.session_state.history.append((prompt, response))
        st.info(f"Answer: {response}")

    with st.expander('Question History'):
        for prompt, response in reversed(st.session_state.history):
            st.info(f"Question: {prompt}")
            st.info(f"Answer: {response}")

# Method for scraping text from pdf files given an uploaded file
def pdf_scrape(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            return text
        else:
            return "Uploaded file is not a PDF."
    except Exception as e:
        print(e)
        return f"Failed to retrieve text from the PDF: {e}"

# Method for scraping text from articles/blogs given a link
def web_scrape(url: str):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"

if __name__ == "__main__":
    main()