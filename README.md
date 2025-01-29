# ontology-semantic-map-with-llm

# Ontology-Based Game Recommendation & Query System

## Overview
This project consists of two phases that work together to provide an ontology-driven game recommendation system with a chatbot for querying data using SPARQL.

- **First Phase:** A Flask-based web application that utilizes RDF and OWL ontology for game recommendations.
- **Second Phase:** A chatbot interface powered by the Groq API, allowing users to query ontology data in natural language.

---
## First Phase: Ontology-Based Game Recommendation
### Description
The first phase of this project is a Flask web application that uses an OWL ontology file to filter and recommend games based on user-selected criteria, such as platform, genre, and difficulty. It utilizes SPARQL queries to extract relevant game recommendations.

### Setup Instructions
1. **Clone the Repository**
   ```sh
   git clone https://github.com/satilmiskabasakal0/ontology-game-recommendation.git
   cd ontology-game-recommendation
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```sh
   python first_phase.py
   ```
   The application will run at `http://127.0.0.1:5051/`

4. **Usage**
   - The web interface allows users to select game preferences.
   - The system will filter and return relevant game recommendations based on the ontology data.

---
## Second Phase: SPARQL Query Chatbot with Groq API
### Description
The second phase extends the functionality of the first phase by integrating a chatbot powered by the Groq API. This chatbot allows users to interact with the ontology-based knowledge system using natural language queries.

### Prerequisites
- **Groq API Key**
  - To use the chatbot, you need to obtain a **Groq API key** from [Groq's website](https://groq.com/).
  - Once obtained, create a `.env` file in the project directory and add your API key:
    ```sh
    GROQ_API_KEY=your_api_key_here
    ```

### Setup Instructions
1. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```sh
   python second_phase.py
   ```
   The chatbot will be accessible at `http://127.0.0.1:5050/`

3. **Usage**
   - The chatbot allows users to ask questions based on the ontology knowledge base.
   - The bot provides relevant answers using the Groq API.

---
## Project Structure
```
/
│── first_phase.py         # Flask application for game recommendation
│── second_phase.py        # Flask chatbot with Groq API integration
│── json-ontology.jsonld   # Ontology file
│── dummytext.txt          # Knowledge base for chatbot
│── .env                   # API key storage (add manually)
│── requirements.txt       # Python dependencies
```

---
## Notes
- Ensure that the ontology file `json-ontology.jsonld` is correctly formatted and available in the project directory.
- For the second phase, the chatbot relies on `dummytext.txt` as a static knowledge base.
- Modify `dummytext.txt` to include domain-specific information for better responses.
- You can deploy both phases separately or integrate them within a single application.


