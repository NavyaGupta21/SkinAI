# ✨ SkinAI: Personalized Skincare Consultant

![Status](https://img.shields.io/badge/Status-Live-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.41-FF4B4B) ![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange)

**SkinAI** is an AI-powered web application developed for the **MACS AIML Project**. It acts as a virtual skincare consultant, using Google's latest **Gemini 2.0 Flash** (via OpenRouter) to analyze facial images and provide instant, personalized skincare advice.

## 🧐 Problem Statement
The skincare market is overwhelmed with products, causing "analysis paralysis." Consumers often misidentify their skin type, leading to incorrect product usage. Professional consultations are often expensive. SkinAI provides a fast, data-driven starting point for a better skincare journey.

## 🚀 Features & USP
* **📸 Multimodal Analysis:** Uses Computer Vision to detect visible skin patterns, texture, and concerns.
* **⚡ 2.0 Speed:** Leverages Gemini 2.0 Flash for near-instant responses (under 10s).
* **🧪 Ingredient Science:** Suggests active ingredients like Salicylic Acid, Hyaluronic Acid, or Retinol based on visual cues.
* **🔒 Secure & Ephemeral:** Images are processed via Base64 encoding and are not stored, ensuring user privacy.

## 🧠 Technology Stack
| Component            | Technology Used |
|----------------------|-----------------|
| **Frontend/UI** | Streamlit (1.41.1) |
| **AI Model** | Gemini 2.0 Flash (OpenRouter API) |
| **Image Processing** | Pillow (PIL) |
| **Language** | Python 3.10+ |

## 📂 Repository Structure
```text
SkinAI/
├── .streamlit/          # Streamlit configuration
│   └── secrets.toml     # API Keys (Local testing)
├── Skincare.py          # Main Application Logic
├── requirements.txt     # Dependencies (openai, streamlit, Pillow)
└── README.md            # Project Documentation