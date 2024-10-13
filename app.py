import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

st.title("RAG App Demo")

urls = [
    'https://michiganvalue.org/',
    'https://michiganvalue.org/about-us/',
    'https://michiganvalue.org/mvc-data/',
      'https://michiganvalue.org/p4p-program/', 
      'https://michiganvalue.org/engagement/',
        'https://michiganvalue.org/value-based-initiatives/',
          'https://michiganvalue.org/upcoming-events/',
            'https://michiganvalue.org/resources-2/', 
            'https://michiganvalue.org/mvc-blog/'
]
loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

# Split the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)
all_splits = docs

# Cache the vectorstore to avoid reinitialization on every interaction
@st.cache_resource
def initialize_vectorstore(_all_splits):
    return Chroma.from_documents(documents=_all_splits, embedding=OpenAIEmbeddings(), persist_directory="./chroma_db")

vectorstore = initialize_vectorstore(all_splits)

# Set up the retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# Initialize the language model
llm = OpenAI(temperature=0.4, max_tokens=500)

# Get the user input
query = st.chat_input("Ask me anything:")

if query:
    # Define the system prompt
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise.\n\n{context}"
    )

    # Create the prompt template
    prompt = ChatPromptTemplate.from_template(system_prompt)

    # Generate the response
    try:
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        response = rag_chain.invoke({"input": query})
        st.write(response["answer"])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
