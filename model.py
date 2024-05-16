import replicate
import os
import logging
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the Replicate API token from the environment
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

# Set up logging
logging.basicConfig(
    filename='example.log',
    filemode='w', 
    level=logging.DEBUG,
    format='%(levelname)s::%(asctime)s::%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
http_client_logger = logging.getLogger('http.client')
http_client_logger.setLevel(logging.DEBUG)
http_client_logger.propagate = True

logger = logging.getLogger()

logger.info("Script started")

def predict(input_prompt: str) -> str:
    model_version = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
    logger.debug(f"Running model version: {model_version} with prompt: {input_prompt}")
    try:
        prediction = replicate.run(
            model_version,
            input={"prompt": input_prompt}
        )
        #logger.debug(f"Prediction output: {prediction}")
        return prediction[0]
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return None

# Get the prompt from the user
prompt = input("Please enter prompt: ")
logger.info(f"User entered prompt: {prompt}")

# Make the prediction and print the result
result = predict(prompt)
if result:
    logger.info(f"Prediction result: {result}")
    print(result)
else:
    logger.error("Failed to get a prediction result")
