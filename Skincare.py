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
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

def reset_everything():
    st.session_state.messages = []
    st.session_state.report_ready = False
    st.session_state.uploaded_image = None
    st.rerun()

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

st.markdown("<h1 style='text-align: center;'>✨ SkinAI ✨</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by <b>Navya Gupta</b></p>", unsafe_allow_html=True)

st.divider()

col1, col2=st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📸 Upload Image")
    if st.session_state.uploaded_image is None:
        uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            st.session_state.uploaded_image = Image.open(uploaded_file)
            st.rerun()
    
    if st.session_state.uploaded_image:
        st.image(st.session_state.uploaded_image, width=150)
        
        if st.button("🚀 Start SkinAI"):
            try:
                with st.spinner("🤖 SkinAI is processing..."):
                    processed_img = encode_image(st.session_state.uploaded_image)
                    prompt = """
                        Act as a professional Dermatologist. Analyze this skin image and provide a report in the following EXACT Markdown format:
                            
                            ### 📋 SkinAI Analysis Report

                            | **Category** | **Details** |
                            | :--- | :--- |
                            | **Skin Type** | (Identify Type) |
                            | **Fitzpatrick Scale** | (Type I-VI) |
                            | **Primary Concerns** | (Bullet points) |


                            ### 🧴 Recommended Targeted Routine

                            **☀️ AM (Protection & Brightening)**
                            1. (Step-by-step)

                            **🌙 PM (Repair & Barrier Support)**
                            1. (Step-by-step)


                            ### 🧪 **Key Active Ingredients**
                            * **Ingredient Name:** (Why it was chosen)

                        Keep the total response under 200 words. Be professional and clear.
                    """
                        
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
            
        if st.button("🗑️ Reset"):
            reset_everything()

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
                    context_memory = [
                        AIMessage(content=f"Context: {st.session_state.messages[0]['content']}"),
                        HumanMessage(content=user_prompt)
                    ]
                    
                    resp = model.invoke(context_memory)
                    st.write(resp.content)
                    st.session_state.messages.append({"role": "assistant", "content": resp.content})
                except Exception as e:
                    st.error(f"Error:{e}")
    else:
        st.info("Upload an image and start SkinAI to see the report here.")