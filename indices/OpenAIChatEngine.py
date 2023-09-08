import openai


class OpenAIChatEngine:
    def __init__(self):
        self.messages = []

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})
        return reply
