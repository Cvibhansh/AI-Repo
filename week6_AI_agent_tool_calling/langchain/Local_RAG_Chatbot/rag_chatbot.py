import json

from retriever import (
    retrieve,
    build_context
)

from langchain_core.prompts import (
    PromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from langchain_community.llms import (
    Ollama
)

llm = Ollama(
    model="qwen2.5:7b"
)

prompt = (
    PromptTemplate.from_template(
"""
You are an enterprise AI support assistant.

Answer the user's question ONLY using the provided context.

If the answer cannot be found in the context,
say:
"I could not find this information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
    )
)

chain = (
    prompt
    | llm
    | StrOutputParser()
)

print(
    "\nEnterprise RAG Chatbot"
)

print(
    "Type 'exit' to quit.\n"
)



while True:

    question = input(
        "You: "
    )

    if (
        question.lower()
        ==
        "exit"
    ):
        break

    history = []
    history.append(
    question
)
    history = history[
    -3:
]

    matches = retrieve(
        question,
        top_k=3
    )

    context = build_context(
        matches
    )

    answer = (
        chain.invoke(
            {
                "context":
                context,

                "question":
                question
            }
        )
    )

    print(
        "\nRetrieved Documents:"
    )
    print(
    context
)

    for match in matches:

        print(
            f"- "
            f"{match['file']} "
            f"(Score: "
            f"{match['score']:.3f})"
        )

    print(
        "\nAI Answer:\n"
    )

    print(
        answer
    )

    print()

    import datetime
    log_entry = {
    "timestamp":
    str(
        datetime.datetime.now()
    ),

    "question":
    question,

    "retrieved_files":
    [
        match["file"]
        for match
        in matches
    ],

    "answer":
    answer
}
    with open(
        "rag_log.json",
        "a",
        encoding="utf-8"
) as file:
        file.write(
        json.dumps(
            log_entry
        )
    )
        file.write(
        "\n"
    )