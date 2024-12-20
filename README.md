# NLP API with FastAPI

This is a simple RESTful API built with FastAPI to serve an NLP model.

## Features
- Predict text using a dummy NLP model
- Easy to extend for real-world NLP models

## Setup Instructions

```bash
conda install python=3.10
conda remove --name question_classification --all
conda create --name question_classification python=3.10
conda activate question_classification

```

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/my-nlp-api.git
   cd my-nlp-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   bash uvicorn_start.sh
   ```

4. **Test the application**:
   ```bash
   pytest
   ```

## Docker Usage

1. **Build the Docker image**:
   ```bash
   docker build -t my-nlp-api .
   ```

2. **Run the container**:
   ```bash
   docker run -it -p 8000:8000 -v `"C:\Users\jimwa\construction-question-classifier`":/root/ my-nlp-api bash
   ```


3. Access the API at `http://localhost:8000`.

## Testing

Run the tests using:
```bash
pytest
```
```

---

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my-nlp-api.git
   cd my-nlp-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   bash uvicorn_start.sh
   ```

4. Open your browser or use a tool like `curl` or Postman to access the API:
   - Root endpoint: `http://localhost:8000/`
   - Prediction endpoint: `POST http://localhost:8000/predict/` with JSON payload `{"text": "some text"}`.

---

### Testing Instructions
Run the tests using `pytest`:
```bash
pytest
```

Example output:
```plaintext
================================= test session starts ==================================
collected 2 items

app/tests/test_main.py ..                                                 [100%]

================================= 2 passed in 0.02s ==================================
```