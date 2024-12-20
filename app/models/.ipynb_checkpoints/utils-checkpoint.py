from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
import numpy as np

def select_representative_questions(questions, k):
    """
    Select K most representative questions from a list of questions.

    Parameters:
    - questions (list): List of question strings.
    - k (int): Number of representative questions to select.

    Returns:
    - list: K most representative questions.
    """
    if len(questions) <= k:
        return questions  # If fewer than K questions, return all of them
    
    # Step 1: Encode questions into embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Load a pre-trained model
    embeddings = model.encode(questions)

    # Step 2: Apply K-means clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(embeddings)

    # Step 3: Select the representative question for each cluster
    representative_questions = []
    for cluster_id in range(k):
        # Find indices of questions in the current cluster
        cluster_indices = np.where(kmeans.labels_ == cluster_id)[0]
        
        # Find the question closest to the cluster center
        cluster_center = kmeans.cluster_centers_[cluster_id]
        closest_idx = cluster_indices[np.argmin(
            np.linalg.norm(embeddings[cluster_indices] - cluster_center, axis=1)
        )]
        representative_questions.append(questions[closest_idx])
    
    return representative_questions
