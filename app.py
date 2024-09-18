import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Cohere API
cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

# Extract text from uploaded PDF files
def extract_pdf_text(pdf_files):
  text = ""
  for pdf in pdf_files:
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
      text += page.extract_text()
  return text

# Split the extracted text into manageable chunks
def split_text_into_chunks(text):
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=10000, chunk_overlap=1000)
  chunks = text_splitter.split_text(text)
  return chunks

# Handle user question input and provide an answer
def handle_user_query(user_question, context_chunks):
  context = " ".join(context_chunks)
  prompt = f"""
    You are helpful AI Assistant designed to help analyse a PDF.
    Use the provided context to assist in extracting relevant information
    and performing analysis tasks. If the information is not present in the
    context, simply state that the data is unavailable.
    Follow these rules at all times:
    - Do not access or refer to personal information outside the scope of the
      provided context.
    - Limit your assistance to the content of the context and queries
      related directly to them.
    - Stick strictly to factual and verifiable information provided in the
      context. Avoid assumptions or interpretations beyond the data presented.

    Context:
    {context}

    Question:
    {user_question}

    Answer:
  """
  response = cohere_client.generate(
    model='command-xlarge-nightly',
    prompt=prompt,
    max_tokens=200
  )

  st.write("Reply:", response.generations[0].text)

def main():
  st.set_page_config(page_title="ChatPDF 💬📄", page_icon="💬")
  st.header("ChatPDF 💬📄")
  st.markdown(
    r"""
      <style>
        .stAppDeployButton {
          visibility: hidden;
        }
        #MainMenu {
          visibility: hidden;
        }
      </style>
    """, unsafe_allow_html=True
  )

  user_question = st.text_input("Ask a question related to the uploaded PDF")

  if user_question and 'context_chunks' in st.session_state:
    handle_user_query(user_question, st.session_state['context_chunks'])

  with st.sidebar:
    st.title("Menu:")
    pdf_files = st.file_uploader(
      "Upload PDF Files", accept_multiple_files=True)

    if st.button("Submit & Process"):
      with st.spinner("Processing..."):
        raw_text = extract_pdf_text(pdf_files)
        context_chunks = split_text_into_chunks(raw_text)
        st.session_state['context_chunks'] = context_chunks
        st.success("Processing complete!")

if __name__ == "__main__":
  main()
