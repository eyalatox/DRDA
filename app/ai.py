import openai

openai.api_key = "sk-YhgtzTRrES0uWI6INlVfT3AlbkFJkyTWq2BA6vu9mxTzqPuy"

# Specify the model and prompt
model = "text-davinci-003"
prompt = "Once upon a time, there was a brave knight who went on a quest to..."

# Send the request
completion = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated text
print(completion.choices[0].text)