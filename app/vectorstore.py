from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from app.loaders import load_csv
from app.splitter import split_documents
from app.embeddings import get_embedding, get_embeddings


class GeminiEmbeddings(Embeddings):

    def embed_documents(self, texts):
        return get_embeddings(texts, batch_size=100)

    def embed_query(self, text):
        return get_embedding(text)


def create_vectorstore():

    print("Loading property data...")

    documents = load_csv("data/property_data.csv")

    # Free Gemini API ke liye testing dataset
    documents = documents[:100]

    print(f"Loaded properties: {len(documents)}")

    # CSV mein har document already ek complete property hai
    chunks = split_documents(
        documents,
        file_type="csv"
    )

    print(f"Documents to embed: {len(chunks)}")

    embeddings = GeminiEmbeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


if __name__ == "__main__":

    vectorstore = create_vectorstore()

    vectorstore.save_local("faiss_index")

    print("FAISS vector store created successfully!")