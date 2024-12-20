# Dummy NLP model

from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli")

labels = ["Document Request",
"Material or Product Information",
"Specifications and Standards",
"Installation and Construction Details",
"Ownership or Responsibility",
"Quantities and Progress Tracking",
"Maintenance and Turnover",
"Translation Request",
"Schedule and Timeline",
"Miscellaneous Queries"]


class NLPModel:

    def predict(self, text: str) -> str:
        classification_response = classifier(text, labels)
        result_list = [{'label': label, 'score': score} for label, score in zip(classification_response['labels'], classification_response['scores'])]

        result_list_sorted = sorted(result_list, key=lambda x: x['score'], reverse=True)

        return result_list_sorted

model = NLPModel()