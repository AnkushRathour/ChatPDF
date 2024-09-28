# ChatPDF 💬📄

ChatPDF enables you to upload PDF files and ask questions about the content of those files using LLM, an open-source language model. The app processes PDF files, breaks the text into manageable chunks for question-answering based on the contents of the PDF.

[ChatPDF Live Demo](https://chatwithmultiplepdffiles.streamlit.app/)

## Features:

- Upload multiple PDF files.
- Extract text from the PDFs and split it into chunks.
- Ask questions about the uploaded PDF content and get responses using the LLM model.

## Installation

Follow these steps to install the required dependencies and set up the application.

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package installer)

### Clone the Repository

First, clone this repository to your local machine:
```bash
git clone https://github.com/AnkushRathour/ChatPDF.git
cd ChatPDF
```

### Install Dependencies

Next, create enviornment and install the required Python packages by running:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root directory and add your Cohere API key:

```bash
COHERE_API_KEY = 'cohere_api_key'
```

### Running the Application

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

### Usage

-   Open the app in your web browser by visiting the URL provided in the terminal after running Streamlit.
-   Upload one or more PDF files using the sidebar.
-   After processing the PDFs, type a question in the input box, and the model will respond based on the content of the PDFs.

## Technologies Used

*   **Streamlit**: For building the user interface and web application.
*   **PyPDF2**: For extracting text from PDF files.
*   **LangChain**: For managing and splitting large texts.
*   **Cohere API**: For generating responses using an LLM.

## Contributing

Feel free to contribute by submitting pull requests or reporting issues. Ensure you follow the project guidelines.

## License

This project is licensed under the MIT License.
