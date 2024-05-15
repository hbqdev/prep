import os
from dotenv import load_dotenv
import replicate

# Load environment variables from .env file
load_dotenv()

# Get the Replicate API token
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')

# Set the token in the Replicate client
replicate.Client(api_token=replicate_api_token)

# Example of running a model
output = replicate.run(
    "stability-ai/stable-diffusion",
    input={"prompt": "a futuristic cityscape"}
)
print(output)
