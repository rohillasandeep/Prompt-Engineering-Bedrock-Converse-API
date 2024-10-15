import json
import re

# Sample JSON string that might have issues
json_string = '''{"prompt":"What is Amazon Bedrock?", "category":"AWS Services", "referenceResponse":"Amazon Bedrock is a fully managed service that offers a choice of industry leading foundation models (FMs) along with a broad set of capabilities that you need to build generative AI applications, simplifying development with security, privacy, and responsible AI. With the comprehensive capabilities of Amazon Bedrock, you can experiment with a variety of top FMs, customize them privately with your data using techniques such as fine-tuning and retrieval-augmented generation (RAG), and create managed agents that execute complex business tasks—from booking travel and processing insurance claims to creating ad campaigns and managing inventory—all without writing any code. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with."}'''

def clean_json_string(json_string):
    # Ensure input is a string
    if not isinstance(json_string, str):
        raise ValueError("Input to clean_json_string must be a string.")

    # Step 1: Trim the string (remove leading and trailing whitespace)
    json_string = json_string.strip()

    # Step 2: Replace smart quotes and em-dashes
    json_string = json_string.replace('“', '"').replace('”', '"')
    json_string = json_string.replace('—', '-')
    
    return json_string

# Call the function for testing
if __name__ == "__main__":
    # Clean the JSON string
    cleaned_json_string = clean_json_string(json_string)

    try:
        # Try to load the cleaned JSON
        parsed_json = json.loads(cleaned_json_string)
        print("Parsed JSON:", parsed_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
