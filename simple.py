import replicate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variables
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

#model_version = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
model_version="meta/meta-llama-3-8b"

# Ask the user for a prompt
prompt = input("Please enter a prompt for the model: ")

# Define the input data
input_data = {"prompt": prompt}

# Run the model
output = replicate.run(model_version, input=input_data)

# Print the output URL
print(output[0])
