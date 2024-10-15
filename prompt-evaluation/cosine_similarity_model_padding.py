from sklearn.metrics.pairwise import cosine_similarity
import boto3, json
import numpy as np
from sklearn.preprocessing import normalize


# Create a session with AWS and initialize a Bedrock client for conversational AI models
session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

def get_vectors(text):
    try:
        if text.strip() != '':
            text = text.strip()
        # Call the Bedrock API to get embeddings
        response = bedrock.invoke_model(
            body=json.dumps({
                'inputText': text
            }),
            modelId="amazon.titan-embed-text-v2:0",
            accept="application/json",
            contentType="application/json",
        )
        response_body = json.loads(response.get("body").read())
        
        # Return the embedding vector
        return response_body.get("embedding")
    
    except boto3.exceptions.Boto3Error as boto_err:
        print(f"Error with AWS Bedrock API: {boto_err}")
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("embedding$$$$$: "+text)
    
    return None

def compute_cosine_similarity(ground_truth_data, completion_data):
    try:
        # Example embeddings for golden data (reference responses)
        golden_embeddings = np.array([get_vectors(ground_truth_data)])
        if golden_embeddings is None:
            raise ValueError("Failed to generate embeddings for golden data")

        # Example embeddings for LLM-generated responses
        llm_embeddings = np.array([get_vectors(completion_data)])
        if llm_embeddings is None:
            raise ValueError("Failed to generate embeddings for completion data")

        # Function to pad embeddings with zeros
        def pad_embeddings(shorter_embeddings, target_length):
            num_missing = target_length - len(shorter_embeddings)
            padding = np.zeros((num_missing, shorter_embeddings.shape[1]))  # Zero vectors for padding
            return np.vstack([shorter_embeddings, padding])

        # Determine the target length (max length of both arrays)
        target_length = max(len(golden_embeddings), len(llm_embeddings))

        # Pad shorter array
        if len(golden_embeddings) < target_length:
            golden_embeddings = pad_embeddings(golden_embeddings, target_length)
        if len(llm_embeddings) < target_length:
            llm_embeddings = pad_embeddings(llm_embeddings, target_length)

        # Normalize embeddings
        golden_embeddings_normalized = normalize(golden_embeddings)
        llm_embeddings_normalized = normalize(llm_embeddings)

        # Compute cosine similarity for each corresponding pair of embeddings
        pairwise_similarities = []
        for golden, llm in zip(golden_embeddings_normalized, llm_embeddings_normalized):
            sim = cosine_similarity([golden], [llm])  # Compute cosine similarity for each pair
            pairwise_similarities.append(sim[0][0])  # Extract the value from the matrix

        # Compute cosine similarities between each pair (golden vs all LLM embeddings)
        pairwise_similarities = []
        for i, golden in enumerate(golden_embeddings_normalized):
            similarities = cosine_similarity([golden], llm_embeddings_normalized)  # Compare against all LLM embeddings
            max_sim_index = np.argmax(similarities)  # Find the index of the most similar LLM embedding
            max_similarity = similarities[0][max_sim_index]  # Get the highest similarity score
            pairwise_similarities.append((i, max_sim_index, max_similarity))  # Store the indices and similarity score
            #print(f"Max similarity for pair {i}: {max_similarity}")
            
        return pairwise_similarities

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred during similarity computation: {e}")

    return None
