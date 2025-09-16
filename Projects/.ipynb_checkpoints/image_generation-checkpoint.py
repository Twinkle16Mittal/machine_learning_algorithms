import streamlit as st
from google.cloud import aiplatform
from vertexai.preview.vision_models import ImageGenerationModel
from PIL import Image
from io import BytesIO
import base64

st.title("AI Image Generator (Google Imagen)")

user_prompt = st.text_input("Enter a prompt for the image:")

if st.button("Generate Image"):
    if not user_prompt:
        st.warning("Please enter a prompt!")
    else:
        try:
            model = ImageGenerationModel.from_pretrained("imagegeneration@006")

            response = model.generate_images(
                prompt=user_prompt,
                number_of_images=1,
                size="1024x1024"
            )

            for img in response.images:
                img_bytes = img._image_bytes  # raw bytes
                image = Image.open(BytesIO(img_bytes))
                st.image(image, caption="Generated Image")

        except Exception as e:
            st.error(f"Error generating image: {e}")
