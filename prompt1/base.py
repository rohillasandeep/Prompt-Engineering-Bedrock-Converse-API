import boto3, json
from utils import create_complete_prompt, pretty_print, Models

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": create_complete_prompt("prompt.txt", "user-query.txt") } 
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId=Models.Sonnet.value,
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']["content"][0]["text"]

print(pretty_print(response_message))