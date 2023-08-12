import openai


openai.api_key = "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"

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=[{"role":"user", "content":"Write an essay on Penguins"}])

print(completion.choices[0].message.content)
