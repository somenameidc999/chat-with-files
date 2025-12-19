### 🧠 File with Files: AI-Powered Document Intelligence

File with Files is a streamlined RAG (Retrieval-Augmented Generation) application that transforms your static PDF documents into interactive conversation partners. By leveraging Google’s Gemini Pro, this tool allows you to extract insights, summarize complex papers, and find specific information within seconds.

---

### ✨ Key Features
* **Instant Document Parsing**: Upload multiple PDFs and begin querying immediately.

* **Contextual Intelligence**: Powered by Google Gemini for high-accuracy, nuanced responses.

* **Clean UI**: Built with Streamlit for a fast, intuitive, and responsive user experience.

* **Local Execution**: Designed for easy setup and testing using the modern `uv` Python package manager.

---

### 🛠️ Tech Stack
* **LLM**: Google Gemini AI

* **Frontend**: Streamlit

* **Environment Management**: uv

---

### 🚀 Getting Started
* **Prerequisites**
  * Before running the project, ensure you have an API Key from the Google AI Studio.

* **Installation & Run**
  * This project uses uv for lightning-fast dependency management. You don't even need to manually create a virtual environment; just run:
    ```
    uv sync
    uv run streamlit run main.py
    ```
---
### 💡 How it Works
* **Ingest**: The app reads and chunks your PDF text.

* **Embed**: Text is converted into vector embeddings (numerical representations).

* **Retrieve**: When you ask a question, the app finds the most relevant "chunks."

* **Augment**: Gemini uses those chunks to provide an accurate, grounded answer.