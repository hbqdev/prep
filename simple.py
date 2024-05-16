import replicate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variables
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

#model_version = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
#model_version="meta/meta-llama-3-8b"

# Ask the user for a prompt
#prompt = input("Please enter a prompt for the model: ")

# Define the input data
#input_data = {"prompt": prompt}

# Run the model
#output = replicate.run(model_version, input=input_data)

def run_tin_test():
    #model_file= "hbqdev/tin-test:d65a7a69b84d17f12d7c47654b6073f433ce71b31e67f7e359a7ea61303529cd"
    model_file="hbqdev/tin-test2:23a088ba88cfe0163be5dd25ab08184cb509994623d02ae79379d601f73629a3"
    input_data = {"image": open("input.jpg", "rb")}
    output = replicate.run(model_file, input=input_data)
    print(output)
# Print the output URL
#print(output[0])

run_tin_test()
