import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

endpoint = "https://dhanushvasa.cognitiveservices.azure.com/"
key = "G4F0dICZp3VFEFFShnt3SlC2EGxxy2uIgVTLf6uYpPFVLBoa5C1rJQQJ99BBACYeBjFXJ3w3AAALACOG1OoO"

document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))


pdf_path = "usecasetry.pdf"

with open(pdf_path, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        model_id="prebuilt-read",  # Prebuilt model ID for text extraction
        body=f  # Pass the file content as body
    )
    result = poller.result()

print("Analyze result:")
for page in result.pages:
    print(f"Page {page.page_number}:")
    for line in page.lines:
        print(f" - {line.content}")