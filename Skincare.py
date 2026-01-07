import streamlit as st
import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI

st.set_page_config(page_title="SkinAI", layout="wide", page_icon="✨")

def encode_image_to_base64(pil_image):
    pil_image.thumbnail((800, 800))
    buffered = BytesIO()
    if pil_image.mode in ("RGBA", "P"):
        pil_image = pil_image.convert("RGB")
    pil_image.save(buffered, format="JPEG", quality=85)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    .report-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b4b; color: black; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ SkinAI ✨")
st.write("Developed by **Navya Gupta**")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("📸 Upload Section")
    uploaded_file = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=300)
        analyze_btn = st.button("🚀 Start SkinAI")
    else:
        st.info("👆 Upload a clear photo of your face.")

with col2:
    st.subheader("📋 Skin Analysis")
    if uploaded_file and analyze_btn:
        try:
            my_api_key = st.secrets["OPENROUTER_API_KEY"]
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=my_api_key,
                max_retries=3,
            )
        
            prompt = "Act as a skincare consultant. Analyze the image and provide: 1. Skin Type, 2. Visible Concerns, 3. Recommended Routine, 4. Key Ingredients."
        
            with st.status("🤖 SkinAI is processing...", expanded=True) as status:
                st.write("Encoding image data...")
                base64_img = encode_image_to_base64(image)
                st.write("Consulting Vision Language Model...")
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-exp:free",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{base64_img}"
                                    }
                                },
                            ],
                        }
                    ],
                )
                
                result = response.choices[0].message.content
                status.update(label="Analysis Complete!", state="complete", expanded=False)
                
                st.markdown(f'<div class="report-card">{result}</div>', unsafe_allow_html=True)
                
                with st.expander("🛡️ Medical Disclaimer"):
                    st.caption("This analysis is for advisory purposes only and does not constitute medical advice.")
            
        except Exception as e:
            st.error(f"Error Details: {e}")
            
    else:
        st.write("Waiting for image analysis...")

st.divider()
st.caption("MACS AIML Project")