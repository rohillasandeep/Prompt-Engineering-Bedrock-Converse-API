# Bedrock-Converse-API

This repository contains a collection of API implementations, prompts, and examples for interacting with Amazon Bedrock's Converse API, which allows you to build conversational agents using generative AI models.

## Overview
The **Bedrock Converse API** enables seamless interaction with various foundation models provided by Amazon Bedrock. This repository includes multiple examples that showcase how to leverage the API to generate conversational responses using prompts, manage system-level interactions, and utilize tools within conversations.

## Repository Contents
The repository contains the following key files and folders:

- **`base.py`**: Basic implementation for initiating a conversation with the Bedrock API.
- **`base_with_image.py`**: Demonstrates how to include image prompts in the conversation flow.
- **`base_with_system.py`**: Focuses on system prompts and how they guide the conversation.
- **`tools-functions/`**: A collection of tools and functions designed for Bedrock's Converse API.
- **`prompts`**: Several prompt examples to handle different conversational contexts:
  - **`prompt-decomposition`**
  - **`prompt1`**
  - **`prompt2-system`**
  - **`prompt3-system-examples`**
- **`house.webp`**: Sample image file used in one of the examples.

## Setup Instructions
To run the examples in this repository, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohillasandeep/Bedrock-Converse-API.git
   cd Bedrock-Converse-API
  
2. **Clone the repository**: Ensure you have Python installed, then install necessary dependencies using pip:
    ```bash
    pip install -r requirements.txt

**File Details**

- base.py: A basic conversation example.
- base_with_image.py: Incorporates image prompts into conversations.
- base_with_system.py: Demonstrates the use of system prompts to direct the conversation's flow.
- prompts/: Different examples of conversation prompts to test and fine-tune responses based on system prompts and other variables.
- prompt-decomposition/: Notebook showcasing example of increased performance / reduced latency when working with very large context windows
- prompt-evaluation/: showcases example of evaluating prompts by ranking them through consin using [skitlearn](https://scikit-learn.org/). use-case discussed evaluates results of completions of various teams participating in a hackathon against golden dataset.
