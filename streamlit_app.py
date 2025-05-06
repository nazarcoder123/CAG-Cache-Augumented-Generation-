import streamlit as st
import requests
import json
from pathlib import Path

# Constants
API_URL = "http://localhost:8000/api/v1"
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Hindi": "hi",
    "Sinhala": "si"
}

def main():
    st.title("Cache-Augmented Generation System")
    st.write("Upload PDFs and ask questions about their content")

    # File upload section
    uploaded_files = st.file_uploader("Choose PDF files", type=['pdf'], accept_multiple_files=True)
    
    if uploaded_files:
        if st.button("Process PDFs"):
            with st.spinner("Processing PDFs..."):
                files = [("files", file) for file in uploaded_files]
                try:
                    response = requests.post(f"{API_URL}/upload", files=files)
                    if response.status_code == 200:
                        st.success("PDFs processed successfully!")
                        st.session_state.pdfs_processed = True
                    else:
                        st.error(f"Error processing PDFs: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to the server: {str(e)}")

    # Question asking section
    if st.session_state.get('pdfs_processed', False):
        st.subheader("Ask Questions")
        
        # Language selection
        selected_language_name = st.selectbox(
            "Select Language for Response",
            options=list(SUPPORTED_LANGUAGES.keys())
        )
        selected_language = SUPPORTED_LANGUAGES[selected_language_name]

        # Question input
        question = st.text_area("Enter your question:")

        if st.button("Ask"):
            if question:
                with st.spinner("Getting answer..."):
                    try:
                        response = requests.post(
                            f"{API_URL}/ask-question",
                            params={"language": selected_language, "question": question}
                        )
                        if response.status_code == 200:
                            answer = response.json()["response"]
                            st.write("### Answer:")
                            st.write(answer)
                        else:
                            st.error(f"Error getting answer: {response.text}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Error connecting to the server: {str(e)}")
            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()