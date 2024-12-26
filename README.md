# Construction Question Classifier API

This is a simple RESTful API built with FastAPI to serve an NLP model of classifying the questions of constructions.

## Features
- Infer the category of a input question in the domain of construction 

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/construction-question-classifier.git
   cd construction-question-classifier
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
   ```

4. Access the notebooks at `http://localhost:8888/lab`


## Docker Usage

1. **Build the Docker image**:
   ```bash
   docker build -t construction-question-classifier .
   ```

2. **Run the container**:
   ```bash
   docker run -it -p 8888:8888 -v `"C:\Users\jimwa\construction-question-classifier`"://construction-question-classifier construction-question-classifier
   ```



3. Access the notebooks at `http://localhost:8888/lab`

