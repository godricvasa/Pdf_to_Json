import streamlit as st
import api
from pdf2image import convert_from_bytes
from PIL import Image
import io

st.set_page_config(layout="wide")  # Enable wide layout
st.title("📄 File to JSON Converter")

uploaded_file = st.file_uploader(
    "Upload a file (PDF, Word, Image, etc.)",
    type=["pdf", "docx", "png", "jpg", "jpeg"]
)

if uploaded_file:
    st.write("✅ File uploaded successfully!")
    
    # Create two columns
    col1, col2 = st.columns([1, 1])  # Equal width columns

    with col1:
        st.subheader("📜 File Preview")

        if uploaded_file.type == "application/pdf":
            images = convert_from_bytes(uploaded_file.read())
            for img in images[:2]:  # Display first 2 pages
                st.image(img, use_column_width=True)

        elif uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)

        else:
            st.write("📄 Preview not available for this file type.")

    with col2:
        st.subheader("📌 JSON Output")
        
        if st.button("Process File"):
            with st.spinner('Processing your file... This may take a moment.'):
                try:
                    json_output = api.extract_json_from_file(uploaded_file)

                    st.success("Processing complete!")
                    st.json(json_output)
                except Exception as e:
                    st.error(f"❌ Error processing file: {str(e)}")
