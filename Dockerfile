# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /construction-question-classifier

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='facebook/bart-large-mnli')"

# Copy the application code
COPY . /construction-question-classifier

RUN pip install --no-cache-dir jupyterlab


# Expose the port and define the startup command
EXPOSE 8888
CMD ["jupyter-lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
