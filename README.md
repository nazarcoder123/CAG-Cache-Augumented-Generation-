📚 Multilingual PDF Q&A App with Gemini AI
A full-stack AI-powered web application that allows users to upload PDF documents, ask context-based questions, and receive intelligent answers translated into their preferred language. Built with FastAPI, Streamlit, LangChain, and Gemini AI, this project features real-time processing, multilingual support, and memory-optimized document caching.

🌟 Features
🗂️ Multi-PDF Upload: Upload and process multiple PDFs simultaneously.

🌍 Multilingual Support: Translate responses into 13 different languages using Google Translate.

❓ Context-Aware Q&A: Ask questions about uploaded PDFs with answers powered by Gemini AI.

⚡ Fast Response via Caching: Uses memory-based context caching for speed and efficiency.

📄 Advanced PDF Processing: Splits PDFs into 1500-character chunks with 150-character overlap for better context.

🔄 Real-Time Status Updates: Frontend displays upload and processing status with error handling.

🚀 Docker Support: Easily containerized for deployment in any environment.

🧩 Tech Stack
Frontend: Streamlit

Backend: FastAPI

AI Integration: Gemini AI

PDF Processing: LangChain PyPDFLoader

Translation: Google Translate Python API

Python: 3.10+

🛠️ Backend API Endpoints
POST /api/v1/upload: Upload PDF files

GET /api/v1/document-status: Check if documents are processed

POST /api/v1/ask-question: Ask questions about uploaded PDFs and receive translated answers

🔄 Data Flow
mermaid
Copy
Edit
graph TD
A[User Uploads PDFs] --> B[Save to uploads/]
B --> C[Extract Text using PyPDFLoader]
C --> D[Split into Chunks with Overlap]
D --> E[Store in Memory Cache]

F[User Asks Question] --> G[Combine Context from Cache]
G --> H[Send to Gemini AI]
H --> I[Translate Answer]
I --> J[Return Answer to User]
📦 Installation
Clone the repository and follow the setup instructions in the README to run locally or deploy with Docker.
