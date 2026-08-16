from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, file_type="csv"):

    # CSV/XLSX:
    # Each document is already one complete property.
    if file_type in ["csv", "xlsx"]:
        return documents

    # PDF:
    # PDFs need chunking because one page/document
    # can contain a lot of text.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


if __name__ == "__main__":

    from app.loaders import load_pdf

    documents = load_pdf("data/properties.pdf")

    chunks = split_documents(
        documents,
        file_type="pdf"
    )

    print("Original documents:", len(documents))
    print("Total chunks:", len(chunks))

    print("\nFirst chunk:")
    print(chunks[0].page_content)