# Utilizing the sample questions dataset (questions.json) please complete the following tasks: 


## 1. Review the sample questions dataset and manually or programmatically suggest a list of question classifications along with a short description of each classification. Feel free to use NLP techniques (entity recognition, sentence parsing, etc) and/or an LLM if that is your desired approach. Explain/show your methodology along with the result. 

For inspiration here are two example classifications we have considered: 

### a. Document Request: Requesting specific documents or information within a document. 

i. Definition: The 'Document Request' category includes questions that directly seek specific project documents or information within them, such as the latest drawings, RFIs, submittals, or change orders. The language is straightforward and often begins with queries like 'What is,' 'Where can I find,' or 'Who initiated.' Look for the frequent mention of specific types of documents and a focus on their recency, status, or specific details they contain. These inquiries might also ask about actions or decisions related to these documents, like approvals or closures. Also, consider if the question targets specific project elements or areas. Questions that aim to identify, confirm, or acquire detailed information from specific construction project documents are classified under the 'Document Request' category. 

### b. Ownership or Responsibility: Identifying the party or individual responsible for or owning a task or feature. 

i. Definition: Categorize a construction field worker's question as 'Ownership or Responsibility' if it seeks to identify which individual or company is responsible for specific aspects of the construction project. These questions typically start with 'Who' or 'Which,' aiming to pinpoint responsibility for particular project components such as roofing, waterproofing, or architectural services. The inquiries may also ask about the roles of specific individuals or legal ownership of elements within the project. Look for questions that not only seek the name of a responsible party but also might inquire about their qualifications or the range of services they provide. This category includes questions geared towards clarifying who owns or is accountable for various tasks or components in the construction process. If the question aims to determine responsibility or ownership for a specific aspect of the project, it falls under the 'Ownership or Responsibility' category. 

## 2. Create a classification model for the questions using the list you determined above. Please submit the classifier as well as an output of the resulting classifications from the included dataset.

## 3. What learnings, findings, or product suggestions do you glean from your results and this dataset? How could some of these insights lead to improving our RAG or routing layer? Please give us this list in priority order (most important first). 

Please note that our goal isn’t perfect accuracy or an exhaustive list of classifications/labels. We would like to see how you work on a problem like this and what your approach is to solving it.
