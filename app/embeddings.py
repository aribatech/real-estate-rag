import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )


def get_embedding(text: str):
    client = get_client()

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )

    return response.embeddings[0].values


def get_embeddings(texts, batch_size=100):
    client = get_client()

    all_embeddings = []

    for i in range(0, len(texts), batch_size):

        batch = texts[i:i + batch_size]

        print(
            f"Embedding {i + 1}-"
            f"{min(i + batch_size, len(texts))} "
            f"of {len(texts)}"
        )

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=batch,
        )

        all_embeddings.extend(
            [embedding.values for embedding in response.embeddings]
        )

    return all_embeddings


if __name__ == "__main__":

    texts = [
        "3 bedroom house in Lahore",
        "5 marla house for sale in Islamabad",
        "Apartment for sale in Karachi",
    ]

    vectors = get_embeddings(texts)

    print("Number of embeddings:", len(vectors))
    print("Embedding dimensions:", len(vectors[0]))