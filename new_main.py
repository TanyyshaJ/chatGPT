import openai

openai.api_key = ""

messages = []   #a list of messages that the api will recieve
system_msg = input("What type of a chatbot would you like?\n")
messages.append({"role": "system", "content": system_msg})  #the user input is appended to the list

print("Your new assistant is ready!")
while input != "quit()":
    message = input()   #new input for user's message
    messages.append ({"role": "user", "content": message}) #append the input to messages list
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages) #feed messages var with the list that has been expanded with both the first inputs and new input
    reply = response["choices"][0]["messages"]["content"]  
    messages.append({"role": "assistant", "content": reply})  #saves response from ai (answer that chatgpt gives u) to the list so that it remembers what we talked about
    print("\n" + reply + "\n")