import argparse
import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "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"

# Set the endpoint for the request
ENDPOINT = "https://api.openai.com/v1/text-completions"

def generate_completion(prompt, model):
  """Generates a text completion for the given prompt and model.

  Args:
    prompt: str, the prompt for the text completion.
    model: str, the name of the model to use for the text completion.

  Returns:
    str, the generated text completion.
  """
  # Set the request headers
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {API_KEY}"
  }

  # Set the request data
  data = {
      "prompt": prompt,
      "model": model
  }

  # Make the request
  response = requests.post(ENDPOINT, headers=headers, json=data)

  # Get the generated text from the response
  text = response.json()["choices"][0]["text"]

  return text

if __name__ == "__main__":
  # Set up the command line arguments
  parser = argparse.ArgumentParser(description="Generate a text completion using the OpenAI API.")
  parser.add_argument("prompt", type=str, help="The prompt for the text completion.")
  parser.add_argument("model", type=str, help="The name of the model to use for the text completion.")
  args = parser.parse_args()

  # Generate the text completion
  completion = generate_completion(args.prompt, args.model)

  # Print the text completion
  print(completion)
