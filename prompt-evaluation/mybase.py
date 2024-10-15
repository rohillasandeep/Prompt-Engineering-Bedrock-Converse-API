import pandas as pd
import json
import statistics
from readcsv import read_csv_file
from readjson import read_json_file
from cosine_similarity_model_padding import compute_cosine_similarity
def process_similarity(csv_file_path, json_file_path):
    # Read CSV and JSON data
    csv_data = read_csv_file(csv_file_path)
    json_data = read_json_file(json_file_path)

    # Convert the csv_data and json_data to pandas DataFrames
    csv_df = pd.DataFrame(csv_data)
    json_df = pd.DataFrame(json_data)

    # Rename the 'prompt' column in json_df to match 'userinput' for merging
    json_df.rename(columns={'prompt': 'userinput'}, inplace=True)

    # Merge the two DataFrames on the common 'userinput' key
    merged_df = pd.merge(csv_df, json_df, on='userinput', how='inner')

    #print(merged_df)
    print("=============== TEAM ===============")
    print(merged_df['teamname'][1])
    print("====================================")

    # Define a function to extract the message from the JSON string
    def extract_message(json_string):
        try:
            # Parse the JSON string
            json_obj = json.loads(json_string)
            # Return the value of the 'message' field
            return json_obj.get('message')
        except json.JSONDecodeError:
            return None  # Return None if there's an error in decoding

    # Initialize a list to store the similarity scores
    similarity_scores = []

    # Iterating through rows in the merged DataFrame
    for index, row in merged_df.iterrows():
        ground_truth_data = row['referenceResponse']
        completion_data = extract_message(row['result'])
        
        # Compute cosine similarity for the current row
        similarity_results = compute_cosine_similarity(ground_truth_data, completion_data)

        # Trim to the first 10 characters and add "..." if the string is longer than 10 characters
        trimmed_text = row['userinput'][:30] + "..." if len(row['userinput']) > 30 else row['userinput']

        # Collect the similarity scores for the current comparison
        for golden_idx, llm_idx, similarity_score in similarity_results:
            print(f"Similary score: {similarity_score} for {trimmed_text}")
            similarity_scores.append(similarity_score)  # Collect similarity scores

    print("#####################")

    # Calculate and print mean, median, and mode if there are scores
    if similarity_scores:
        mean_similarity = statistics.mean(similarity_scores)
        median_similarity = statistics.median(similarity_scores)

        try:
            mode_similarity = statistics.mode(similarity_scores)
        except statistics.StatisticsError:
            mode_similarity = "No unique mode"

        print(f"Mean of Cosine Similarity: {mean_similarity}")
        print(f"Median of Cosine Similarity: {median_similarity}")
        print(f"Mode of Cosine Similarity: {mode_similarity}")
    else:
        print("No similarity results to calculate statistics.")

# Call the function with the file paths as arguments
if __name__ == "__main__":
    process_similarity('8f3994d0-2620-4075-8af1-6d11b95c50a7_converted-2.csv', 'golden-data.txt')
