# ✨SkinAI: Personalized Skincare Consultant

![Status](https://img.shields.io/badge/Status-Prototype-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.52-FF4B4B) ![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange)

**SkinAI** is an AI-powered web application developed as part of the **MACS AIML Project**. It acts as a virtual skincare consultant, using Google's **Gemini 2.5 Flash** Vision Language Model to analyze facial images and provide instant, personalized skincare advice.

## 🚀 Features & USP
* **📸 Multimodal Analysis:** "Sees" your skin using advanced Computer Vision to detect acne, texture, and dryness.
* **⚡ Instant Results:** Provides a structured report (Skin Type, Concerns, Routine) in under 30 seconds.
* **🧪 Ingredient Science:** Recommends specific chemical ingredients (e.g., Salicylic Acid, Retinol) tailored to your visual analysis.
* **🔒 Privacy First:** Images are processed in-memory and not stored permanently.


## 🧠 Technology Stack
| Component            | Description |
| **Python 3.10+**     | Core backend logic and AI integration |
| **Streamlit**        | Lightweight web interface for rapid prototyping |
| **Gemini 2.5 Flash** | Vision Language Model for image + text understanding |
| **Computer Vision**  | Visual feature extraction from facial images |


## 📂 Project Structure
```text
SkinAI/
├── app.py               # Main application code
├── requirements.txt     # Project dependencies
└── README.md            # Documentation & Guide