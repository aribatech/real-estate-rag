from langchain_community.document_loaders import CSVLoader, PyPDFLoader
from langchain_core.documents import Document
import pandas as pd


def load_csv(file_path: str):
    loader = CSVLoader(file_path=file_path)
    return loader.load()


def load_xlsx(file_path: str):
    df = pd.read_excel(file_path)

    documents = []

    for index, row in df.iterrows():
        content = "\n".join(
            f"{column}: {value}"
            for column, value in row.items()
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file_path,
                    "row": index
                }
            )
        )

    return documents


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()


if __name__ == "__main__":
    csv_docs = load_csv("data/property_data.csv")
    xlsx_docs = load_xlsx("data/property_data.xlsx")
    pdf_docs = load_pdf("data/properties.pdf")

    print("CSV:", len(csv_docs))
    print("XLSX:", len(xlsx_docs))
    print("PDF:", len(pdf_docs))

    print("\nFirst PDF document:")
    print(pdf_docs[0].page_content[:500])