import time
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv, find_dotenv

if "client" not in st.session_state:
    load_dotenv(find_dotenv())
    st.session_state.client = genai.Client()

client = st.session_state.client

def upload_and_index(files):
    uploaded_files = []
    for file in files:
        with st.spinner(f"Uploading {file.name}..."):
            uploaded_file = client.files.upload(
                file=file,
                config={
                    "mime_type": file.type,
                    "display_name": file.name,
                },
            )

            while uploaded_file.state.name == "PROCESSING":
                time.sleep(2)
                uploaded_file = client.files.get(name=uploaded_file.name)
            if uploaded_file.state.name == "FAILED":
                raise ValueError("File processing failed.")

            uploaded_files.append(uploaded_file)
    return uploaded_files

st.title("Chat with files")

uploaded = st.file_uploader(
    "Upload your files",
    type=["pdf", "txt", "docx", "doc", "csv", "xlsx", "xls", "pptx", "ppt", "pps", "ppsx", "json"],
    accept_multiple_files=True,
)

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []
if "chat" not in st.session_state:
    st.session_state.chat = None

if uploaded and st.button("Process Files"):
    st.session_state.uploaded_files = upload_and_index(uploaded)
    if st.session_state.uploaded_files:
        st.session_state.chat = client.chats.create(model="gemini-2.5-flash")
        st.success("Files are ready! Start asking questions below.")

if st.session_state.chat and st.session_state.uploaded_files:
    user_input = st.text_input("Ask a question about your documents")
    if user_input:
        message = list(st.session_state.uploaded_files) + [user_input]
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(message=message)
        st.markdown(f"**Gemini:** {response.text}")
