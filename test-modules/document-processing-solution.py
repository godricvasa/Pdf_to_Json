# from pdf2image import convert_from_path
# import requests

# def ocr_space_file(filename, overlay=False, api_key='K87882274688957', language='eng'):
#     """ OCR.space API request with local file. """
#     payload = {'isOverlayRequired': overlay,
#                'apikey': api_key,
#                'language': language,
#                }
#     with open(filename, 'rb') as f:
#         r = requests.post('https://api.ocr.space/parse/image',
#                           files={filename: f},
#                           data=payload,
#                           )
#     return r.content.decode()

# # Convert PDF to images
# pages = convert_from_path('usecasetry.pdf', 300)  # 300 DPI
# for i, page in enumerate(pages):
#     # Save each page as an image
#     image_filename = f'page_{i}.png'
#     page.save(image_filename, 'PNG')

#     # Process image using OCR.space
#     result = ocr_space_file(filename=image_filename, language='eng')
#     print(result)
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

# Set Azure credentials
key = "G4F0dICZp3VFEFFShnt3SlC2EGxxy2uIgVTLf6uYpPFVLBoa5C1rJQQJ99BBACYeBjFXJ3w3AAALACOG1OoO"  # Replace with your actual API key if not using env variables
endpoint = "https://dhanushvasa.cognitiveservices.azure.com/"  # Replace with your actual endpoint

def analyze_pdf(pdf_path):
    client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Read the PDF file
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    # Make API request
    poller = client.begin_analyze_document("prebuilt-read", document=pdf_data)
    result: AnalyzeResult = poller.result()

    # Extract text
    extracted_text = []
    for page in result.pages:
        for line in page.lines:
            extracted_text.append(line.content)

    # Print extracted text
    extracted_text_str = "\n".join(extracted_text)
    print("Extracted Text:\n", extracted_text_str)

    return extracted_text_str


if __name__ == "__main__":
    pdf_file_path = "usecasetry.pdf"  # Replace with the actual PDF file path
    analyze_pdf(pdf_file_path)
