import streamlit as st
import base64
from io import BytesIO
from PIL import Image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage

st.set_page_config(page_title="SkinAI", layout="wide", page_icon="✨")

api_key=st.secrets["GOOGLE_API_KEY"]
model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            google_api_key=api_key,
            max_retries=2
        )

if "messages" not in st.session_state:
    st.session_state.messages = []
if "report_ready" not in st.session_state:
    st.session_state.report_ready = False

def encode_image(pil_image):
    pil_image.thumbnail((512,512))
    buffered = BytesIO()
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    pil_image.save(buffered, format="JPEG", quality=75)
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

col1, col2=st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📸 Upload Image")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file and not st.session_state.report_ready:
        img = Image.open(uploaded_file)
        st.image(img, width=150)
        
        if st.button("🚀 Start SkinAI"):
            try:
                with st.spinner("🤖 SkinAI is processing..."):
                    processed_img = encode_image(img)
                    prompt = "Analyze this skin image and provide: 1.Skin Type 2.Primary Concerns 3.Routine 4.Key Actives. Bullet points only. Max 150 words."
                    
                    input_msg = HumanMessage(content=[
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{processed_img}"}
                   ])
                    response = model.invoke([input_msg])
                    
                    st.session_state.messages.append({"role": "assistant", "content": response.content})
                    st.session_state.report_ready = True
                    st.rerun()

            except Exception as e:
                st.error(f"Error Details: {e}")

with col2:
    st.subheader("💬 Chat with SkinAI")
    
    if st.session_state.report_ready:
        st.markdown(f'<div class="report-card"><b>SkinAI Analysis Result:</b><br>{st.session_state.messages[0]["content"]}</div>', unsafe_allow_html=True)
        
        with st.expander("🛡️ Medical Disclaimer"):
            st.caption("This analysis is for advisory purposes only and does not constitute medical advice.")
            
        st.write("---")

        for msg in st.session_state.messages[1:]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if user_prompt := st.chat_input("Ask SkinAI about products..."):
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            with st.chat_message("user"): 
                st.write(user_prompt)
            
            with st.chat_message("assistant"):
                try:
                    limited_history = [st.session_state.messages[0]] + st.session_state.messages[-2:]
                    
                    langchain_messages = []
                    for m in limited_history:
                        if m["role"] == "user":
                            langchain_messages.append(HumanMessage(content=m["content"]))
                        else:
                            langchain_messages.append(AIMessage(content=m["content"]))
                    
                    resp = model.invoke(langchain_messages, max_output_tokens=150)

                    st.write(resp.content)
                    st.session_state.messages.append({"role": "assistant", "content": resp.content})
                except Exception as e:
                    st.error("SkinAI is busy. Please try again.")
    else:
        st.info("Upload an image and start SkinAI to see the report here.")