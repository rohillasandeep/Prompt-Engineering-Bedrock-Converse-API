import boto3, json

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

with open("./house.webp", "rb") as image_file:
    image_bytes = image_file.read()

message_list = []

summary_message = {
    "role": "user",
    "content": [
        { "text": "Can you please summarize our conversation so far?" } 
    ],
}

message_list.append(summary_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    system=[
        { "text": "Please respond to all requests in the style of a pirate." }
    ],
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']['content']
print(json.dumps(response_message[0]['text'], indent=4))

