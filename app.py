import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set your Google Generative AI API key
api_key = 'AIzaSyCfUESlBZGqohyJ4bkb1RZ8pwTn2sRLPKI'
genai.configure(api_key=api_key)

# Function to process the prompt or image and generate AI response
def generate_content(prompt=None, image=None):
    if prompt:
        try:
            # Generate AI content based on text prompt
            response = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0827').generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Failed to generate content: {str(e)}"
    elif image:
        try:
            # Process image and generate content (if applicable)
            img = Image.open(image)
            # For simplicity, assuming the model can generate content from image (adjust per your needs)
            response = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0827').generate_content(img)
            return response.text
        except Exception as e:
            return f'Failed to process image: {str(e)}'
    else:
        return "No valid input provided."

# Streamlit app layout
st.set_page_config(page_title="AI Content Generator", layout="wide")

# Header Section
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>AI Content Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Generate creative responses from text prompts or images using AI</p>", unsafe_allow_html=True)

# Input Section in two columns
col1, col2 = st.columns(2)

with col1:
    prompt = st.text_area("Enter a Text Prompt", placeholder="Ask the AI anything...")

with col2:
    uploaded_image = st.file_uploader("Upload an Image (Optional)", type=["jpg", "jpeg", "png"])

# Button to generate content
if st.button("Generate Content", key="generate"):
    if prompt or uploaded_image:
        with st.spinner('Generating content...'):
            result = generate_content(prompt, uploaded_image)
        
        # Display results beautifully
        st.markdown("---")  # Divider
        st.markdown("<h3 style='color: #007BFF;'>Generated Content</h3>", unsafe_allow_html=True)

        # Text response styling
        if result:
            st.markdown(f"<div style='padding: 20px; background-color: #F0F0F0; border-radius: 5px; color: #333;'>{result}</div>", unsafe_allow_html=True)
    else:
        st.error("Please provide a prompt or upload an image.")

# Add some space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
