import replicate

# Define the model and the input
model_version = "meta/meta-llama-3-70b-instruct"
input_data = {"prompt": "Please write a haiku about llamas."}

# Stream the output
for event in replicate.stream(model_version, input=input_data):
    print(str(event), end="")
