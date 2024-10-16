# Bedrock-Converse-API

This repository contains a collection of API implementations, prompts, and examples for interacting with Amazon Bedrock's Converse API, which allows you to build conversational agents using generative AI models.

## Overview
The **Bedrock Converse API** enables seamless interaction with various foundation models provided by Amazon Bedrock. This repository includes multiple examples that showcase how to leverage the API to generate conversational responses using prompts, manage system-level interactions, and utilize tools within conversations.

## Repository Contents
The repository contains the following key files and folders:

- **`base.py`**: A basic implementation for initiating a conversation with the Bedrock API.
- **`base_with_image.py`**: Demonstrates how to include image prompts in the conversation flow.
- **`base_with_system.py`**: Focuses on system prompts and how they guide the conversation.
- **`tools-functions/`**: A collection of utility functions and tools designed to enhance the use of the Bedrock Converse API.
- **`prompts/`**: Examples of various prompt designs to handle different conversational scenarios:
  - **`prompt-decomposition/`**: An example demonstrating how to improve performance and reduce latency with large context windows in conversations.
  - **`prompt-evaluation/`**: A prompt evaluation example using cosine similarity with [scikit-learn](https://scikit-learn.org/), evaluating results from a hackathon against a golden dataset.
  - **`prompt1`**, **`prompt2-system`**, **`prompt3-system-examples`**: Examples showcasing different conversation flows and system-guided interactions.
- **`house.webp`**: A sample image file used in some image prompt examples.

## Setup Instructions
To run the examples in this repository, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohillasandeep/Bedrock-Converse-API.git
   cd Bedrock-Converse-API
  
2. **Clone the repository**: Ensure you have Python installed, then install necessary dependencies using pip:
    ```bash
    pip install -r requirements.txt

3. Setup AWS CLI if executing workshop outside of AWS Environment otherwise use IAM Roles/Permissions on the EC2/SageMaker Studio
   ```bash
   Setup AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html
   Assign Role to EC2: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#generate-policy-for-iam-role
   Execution Roles for SageMaker Studio:  https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html

**File Details**

- base.py: A basic conversation example.
- base_with_image.py: Incorporates image prompts into conversations.
- base_with_system.py: Demonstrates the use of system prompts to direct the conversation's flow.
- prompt*/: Different examples of conversation prompts to test and fine-tune responses based on system prompts and other variables.
- prompt-decomposition/: A notebook that demonstrates increased performance and reduced latency when working with large context windows.
- prompt-evaluation/:A prompt evaluation example that uses cosine similarity, powered by [skitlearn](https://scikit-learn.org/). to rank and compare different team submissions from a hackathon against a golden dataset.
