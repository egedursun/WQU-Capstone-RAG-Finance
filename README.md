# WQU-Capstone-RAG-Finance
WQU Capstone Project, November 2023.


## Project Description

This project is a part of the WorldQuant University Capstone Project. 
The project aims to develop an GPT-Powered RAG Chatbot for Financial Applications.
The agent aims to retrieve data from various resources regarding fundamental and technical data,
and provide summary and analysis of the data in a conversational manner.

## Steps to Run

1. Clone the repository
2. Install the requirements -> `pip install -r requirements.txt`
3. Create the `.env` file.
4. Fill the required parameters:
```
OPENAI_API_KEY=''
WEAVIATE_URL=''
WEAVIATE_API_KEY=''
POLYGON_API_URL=''
POLYGON_API_KEY=''
```

5. Run the `main.py` file -> `python main.py`
6. The chatbot will be available at `http://localhost:5000/` via Streamlit server.


## Project Structure

```

├── README.md
├── functions
│   ├── ...
├── knowledge
│   ├── vector
│   │   ├── WeaviateClient
│── llm
│   ├── ChatMemory
├── models
├── ingestion
│   ├── document
│   │   ├── ...
│   ├── data_models
│   │   ├── ...
│   │── http_models
│   │   ├── ...
│── tools
│   ├── container
│   │   ├── ...
│   ├── test
│   │   ├── ...
│   ├── PolygonAPIClient
│   ├── ToolManager

```


## Author

- [Ege Dogan Dursun](https://cv-page.onrender.com)
