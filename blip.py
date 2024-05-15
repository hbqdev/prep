import replicate
import os
from dotenv import load_dotenv
load_dotenv()

# Get the Replicate API token
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')
# Define the model version and the input file
model_version = "andreasjansson/blip-2:f677695e5e89f8b236e52ecd1d3f01beb44c34606419bcc19345e046d8f786f9"
input_data = {"image": "https://tse1.mm.bing.net/th?id=OIP.jTE__cmysmzZ0II90oD0PwHaLI&pid=15.1"}

# Run the model
output = replicate.run(model_version, input=input_data)
print(output)