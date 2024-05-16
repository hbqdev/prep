import replicate
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

def predict(input_prompt: str) -> str:
    model_version = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
    prediction = replicate.run(
        model_version,
        input={"prompt": input_prompt}
    )
    return prediction[0]

prompt = input("Please enter prompt: ")
print(predict(prompt))
