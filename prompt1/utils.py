# file_reader.py
import textwrap

from enum import Enum

class Models(Enum):
    # Enum for storing model identifiers for different AI models.
    # Each member represents a specific model hosted by various platforms like Anthropic and Meta.
    
    Sonnet = "anthropic.claude-3-sonnet-20240229-v1:0"  
    Haiku = "anthropic.claude-3-haiku-20240307-v1:0"   
    Llama = "meta.llama3-8b-instruct-v1:0"         
    Cohere = "cohere.command-r-plus-v1:0" 

def pretty_print(text):
    """
    Pretty prints the given text by handling newlines and formatting.

    :param text: The text to pretty print.
    :return: The formatted text as a string.
    """
    # Use textwrap.fill to format the text
    formatted_text = textwrap.fill(text, width=80, replace_whitespace=False)
    return formatted_text

def read_file_contents(file_name):
    """
    Reads the contents of a local text file and returns it as a string.

    :param file_name: The name of the file to read.
    :return: The contents of the file as a string.
    """
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return f"Error: The file {file_name} was not found."
    except Exception as e:
        return f"Error: An error occurred while reading the file. Details: {e}"

def create_complete_prompt(template_file, content_file):
    """
    Reads the prompt template and content files, replaces the variables in the template with the content,
    and returns the complete prompt.

    :param template_file: The file name of the prompt template.
    :param content_file: The file name of the content to replace in the template.
    :return: The complete prompt as a string.
    """
    # Read the prompt template and content files
    template = read_file_contents(template_file)
    content = read_file_contents(content_file)
    
    # Check if there were errors reading the files
    if template.startswith("Error:") or content.startswith("Error:"):
        return f"Template file error: {template}\nContent file error: {content}"
    
    # Replace the placeholder in the template with the actual content
    complete_prompt = template.replace("{content}", content)
    print(complete_prompt)
    print("+++++++++++++++++++++++++++")
    return complete_prompt

# Example usage:
if __name__ == "__main__":
    file_name = 'example.txt'
    contents = read_file_contents(file_name)
    print(contents)
