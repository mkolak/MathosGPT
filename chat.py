from indices.ComposableGraphChatEngine import ComposableGraphChatEngine
from indices.OpenAIChatEngine import OpenAIChatEngine
from indices import indices
from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.memory import ChatMemoryBuffer
import openai


class Chat:
    def __init__(self, indices):
        if not indices:
            self.engine = OpenAIChatEngine()
        elif type(indices) is list and len(indices) != 1:
            self.engine = ComposableGraphChatEngine(indices)
        else:
            if type(indices) is list:
                index = indices[0]["index"]
            else:
                index = indices["index"]
            llm = OpenAI(model="gpt-3.5-turbo-16k", temperature=0, max_tokens=2048)
            service_context = ServiceContext.from_defaults(llm=llm)
            memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
            self.engine = index.as_chat_engine(
                chat_mode="openai", memory=memory, service_context=service_context
            )


def load_indices(names):
    _indices = []
    for name in names:
        if name == "kadrovi":
            _indices.append(indices.kadrovi)
        if name == "studenti":
            _indices.append(indices.studenti)
        if name == "upisi":
            _indices.append(indices.upisi)
        if name == "kolegiji":
            _indices.append(indices.kolegiji)
        if name == "fakultet":
            _indices.append(indices.fakultet)
        if name == "studiji":
            _indices.append(indices.studiji)
    return _indices


def get_chat_name(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
            {
                "role": "user",
                "content": "S obzirom na postavljeno pitanje definiraj naziv razgovora kao što to radi chatGPT i pritom mi kao odgovor vrati samo naziv, bez ičega drugog",
            },
        ],
    )
    return response["choices"][0]["message"]["content"]
