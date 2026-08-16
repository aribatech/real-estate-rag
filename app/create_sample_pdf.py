import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("data/property_data.csv").head(100)

pdf_path = "data/properties.pdf"

document = SimpleDocTemplate(pdf_path)
styles = getSampleStyleSheet()

content = []

for _, row in df.iterrows():
    property_text = "<br/>".join(
        f"<b>{column}:</b> {value}"
        for column, value in row.items()
    )

    content.append(Paragraph(property_text, styles["BodyText"]))
    content.append(Spacer(1, 12))

document.build(content)

print(f"PDF created: {pdf_path}")