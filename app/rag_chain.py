import os
from dotenv import load_dotenv
from google import genai
from app.retriever import retrieve

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_question(query: str):

    documents = retrieve(query, k=5)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a helpful real estate assistant.

Answer the user's question using ONLY the property information
provided in the context below.

If the answer is not present in the context, say:
"I couldn't find that information in the available property data."

Context:
{context}

User Question:
{query}

Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    question = "Find me a 3 bedroom house in Lahore"

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)