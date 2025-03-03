import re
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import document_Analyzer

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

def chat(prompt):
    """Interacts with Gemini API and extracts valid JSON from its response."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Convert the text to JSON with relatable keys and values: {prompt}")

    raw_text = response.text.strip()

    # Attempt to extract JSON using regex
    match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if match:
        return match.group(0)  # Return the matched JSON-like text
    return raw_text  # Return as is if no JSON is found

def extract_json_from_file(file):
    """Extracts text from a file and converts it to structured JSON."""
    try:
        text = str(document_Analyzer.text_Extractor(file))
        response = chat(text)

        try:
            structured_json = json.loads(response)
            return structured_json  # Return parsed JSON
        except json.JSONDecodeError:
            return {"error": "Failed to parse valid JSON from Gemini response", "raw_response": response}

    except Exception as e:
        return {"error": str(e)}

