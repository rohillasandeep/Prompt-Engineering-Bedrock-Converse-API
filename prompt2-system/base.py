import boto3, json
from utils import create_complete_prompt, pretty_print, read_file_contents, Models

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

system_prompt = read_file_contents("system.txt")

print (system_prompt)


summary_message = {
    "role": "user",
    "content": [
        { "text": create_complete_prompt("prompt.txt", "user-query.txt") } 
    ],
}

message_list.append(summary_message)

response = bedrock.converse(
    modelId=Models.Sonnet.value,
    messages=message_list,
    system=[
        { "text": system_prompt }
    ],
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

print("RESULT: \n\n")
response_message = response['output']['message']["content"][0]["text"]


print(pretty_print(response_message))

