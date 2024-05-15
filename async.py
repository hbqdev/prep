import replicate
import asyncio
# Define the model version
model_version = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"
prompts = [
    f"A chariot pulled by a team of {count} rainbow unicorns"
    for count in ["two", "four", "six", "eight"]
]

# Run the model asynchronously
async def run_model():
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(replicate.async_run(model_version, input={"prompt": prompt}))
            for prompt in prompts
        ]
    results = await asyncio.gather(*tasks)
    return results

# Get the results
#results = asyncio.run(run_model())
print(results)

REPLICATE_API_TOKEN="r8_dcCPeRrlNHZ3kNhQZoLY9d06TtlQ8Ov2ul6Ic"