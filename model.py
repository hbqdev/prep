import replicate
def predict(input: str) -> str:
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("latest")
    prediction = replicate.predictions.create(
        version=version,
        input={"prompt": input}
    )
    return prediction.output
