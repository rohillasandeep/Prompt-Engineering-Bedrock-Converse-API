import boto3, json

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

with open("./house.webp", "rb") as image_file:
    image_bytes = image_file.read()

message_list = []

image_message = {
    "role": "user",
    "content": [
        {"text": "Image 1:"},
        {
            "image": {
                "format": "webp",
                "source": {
                    "bytes": image_bytes  # No base64 encoding required
                }
            }
        },
        {"text": "Please describe the image."}
    ],
}

message_list.append(image_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

response_message = response['output']['message']["content"][0]["text"]

print(response_message)

