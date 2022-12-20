import subprocess
import json

# Set the endpoint and model for the request
endpoint = "https://api.openai.com/v1/text-completions"
model = "text-davinci-002"

# Set the prompt for the request
prompt = "What is the capital of France?"

# Set the API key for the request
api_key = "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"

# Set the request data
# data = f'{"prompt": "{prompt}", "model": "{model}"}'
data = f'{{"prompt": "{prompt}", "model": "{model}"}}'


# Set the request headers
headers = f"-H 'Content-Type: application/json' -H 'Authorization: Bearer {api_key}'"

# Set the command to run
command = f"curl -X POST {headers} -d '{data}' {endpoint}"

# Run the command and capture the output
output = subprocess.run(command, shell=True, capture_output=True)

# Print the output
print(output.stdout)
