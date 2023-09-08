from llama_index import VectorStoreIndex
from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.indices.composability import ComposableGraph


class ComposableGraphChatEngine:
    def __init__(self, indices):
        llm = OpenAI(model="gpt-3.5-turbo-16k", temperature=0, max_tokens=2048)
        service_context = ServiceContext.from_defaults(llm=llm)

        custom_query_engines = {
            elem["index"]
            .index_id: elem["index"]
            .as_query_engine(
                service_context=service_context, similarity_top_k=elem["query_top"]
            )
            for elem in indices
        }

        _indices = [elem["index"] for elem in indices]
        _summaries = [elem["summary"] for elem in indices]

        self.graph = ComposableGraph.from_indices(
            VectorStoreIndex,
            _indices,
            index_summaries=_summaries,
        )

        self.engine = self.graph.as_query_engine(
            custom_query_engines=custom_query_engines
        )

        self.chat_history = []

    def chat(self, message):
        previous = None
        if self.chat_history:
            for msg in reversed(self.chat_history):
                sender = msg["sender"]
                content = msg["content"]
                previous = f"{sender}: {content}\n{previous}"
                if len(previous) > 3000:
                    break
            previous = f"Chat history:\n{previous}"

        self.chat_history.append({"sender": "user", "content": message})

        query = message
        if previous:
            query = f"{previous}\nNew query: {message}"

        response = self.engine.query(query)
        self.chat_history.append({"sender": "chatGPT", "content": response.response})

        return response
