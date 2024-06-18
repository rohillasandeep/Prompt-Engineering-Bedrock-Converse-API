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

response = bedrock.converse_stream(
    modelId=Models.Cohere.value,
    messages=message_list,
    system=[
        { "text":  system_prompt}
    ],
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

print("RESULT: \n\n")

stream = response.get('stream')
if stream:
        for event in stream:
            if 'messageStart' in event:
                print(f"\nRole: {event['messageStart']['role']}")

            if 'contentBlockDelta' in event:
                print(event['contentBlockDelta']['delta']['text'], end="")

            if 'messageStop' in event:
                print(f"\nStop reason: {event['messageStop']['stopReason']}")

            if 'metadata' in event:
                metadata = event['metadata']
                if 'usage' in metadata:
                    print("\nToken usage")
                    print(f"Input tokens: {metadata['usage']['inputTokens']}")
                    print(
                        f":Output tokens: {metadata['usage']['outputTokens']}")
                    print(f":Total tokens: {metadata['usage']['totalTokens']}")
                if 'metrics' in event['metadata']:
                    print(
                        f"Latency: {metadata['metrics']['latencyMs']} milliseconds")

