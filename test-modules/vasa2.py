import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest


# use your `key` and `endpoint` environment variables
key = "G4F0dICZp3VFEFFShnt3SlC2EGxxy2uIgVTLf6uYpPFVLBoa5C1rJQQJ99BBACYeBjFXJ3w3AAALACOG1OoO"  # Replace with your actual API key if not using env variables
endpoint = "https://dhanushvasa.cognitiveservices.azure.com/"
# helper functions
def get_words(page, line):
    result = []
    for word in page.words:
        if _in_span(word, line.spans):
            result.append(word)
    return result


def _in_span(word, spans):
    for span in spans:
        if word.span.offset >= span.offset and (word.span.offset + word.span.length) <= (span.offset + span.length):
            return True
    return False


def analyze_read():
    # sample document
    formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/read.png"

    client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    with open(r"usecasetry.pdf", "rb") as f:
       poller = client.begin_analyze_document(
           "prebuilt-invoice", document=f, locale="en-US"
       )
    # with open(r"usecasetry.pdf", "rb") as f:
    #   poller = client.begin_analyze_document("prebuilt-layout",document=f)
    result: AnalyzeResult = poller.result()
    # poller = client.begin_analyze_document(
    #     "prebuilt-read", AnalyzeDocumentRequest(url_source=formUrl
    # ))
    # result: AnalyzeResult = poller.result()
    
    print(result)
    print(type(result))

if __name__ == "__main__":
    analyze_read()