import openai


openai.api_key = "OPENAI_KEY"

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=[{"role":"user", "content":"Write an essay on Penguins"}])

print(completion.choices[0].message.content)
