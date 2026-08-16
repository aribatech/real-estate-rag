from langchain_community.vectorstores import FAISS
from app.vectorstore import GeminiEmbeddings


def load_vectorstore():
    embeddings = GeminiEmbeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def retrieve(query: str, k: int = 5):
    vectorstore = load_vectorstore()

    results = vectorstore.similarity_search(
        query,
        k=k
    )

    return results


if __name__ == "__main__":
    query = "3 bedroom house in Lahore"

    results = retrieve(query)

    print(f"Found {len(results)} relevant properties:\n")

    for i, document in enumerate(results, 1):
        print(f"--- Result {i} ---")
        print(document.page_content)
        print()