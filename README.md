# ✨ SkinAI: Personalized Skincare Consultant

![Status](https://img.shields.io/badge/Status-Live-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.41-FF4B4B) ![LangChain](https://img.shields.io/badge/Framework-LangChain-green)

**SkinAI** is an AI-powered multimodal web application developed for the **MACS AIML Project**. It acts as a virtual skincare consultant by using **Google Gemini 1.5 Flash** integrated via **LangChain** to analyze facial images and provide data-driven skincare advice through an intelligent, stateful chat interface.

## 🧐 Problem Statement
The skincare market is overwhelmed with products, causing "analysis paralysis." Consumers often misidentify their skin type, leading to incorrect product usage. Professional consultations are often expensive. SkinAI provides a fast, science-based starting point for a better skincare journey.

## 🚀 Features & USP
* **📸 Multimodal Vision Scan:** Processes facial images using Google's Generative AI to identify skin type, concerns, and textures.
* **💬 Stateful Chat Consultant:** Remembers the initial analysis report during follow-up questions using **LangChain's AIMessage/HumanMessage** logic.
* **📉 Token-Efficient Architecture:** Implements a **Context Window Pruning** strategy (keeps the Report + last 2 messages) to minimize token consumption and reduce latency.
* **🔒 Privacy-Focused:** Images are resized to **512x512** and processed in-memory using Base64; no user data or photos are stored on servers.



## 🧠 Technology Stack
| Component            | Technology Used |
|----------------------|-----------------|
| **Frontend/UI** | Streamlit (1.41.1) |
| **Orchestration** | LangChain (langchain-google-genai) |
| **AI Model** | Gemini 1.5 Flash (Google AI Studio) |
| **Image Processing** | Pillow (PIL) |
| **Language** | Python 3.10+ |

## 📂 Repository Structure
```text
SkinAI/
├── .streamlit/          # Streamlit configuration
│   └── secrets.toml     # GOOGLE_API_KEY
├── Skincare.py          # Main Application (LangChain Logic)
├── requirements.txt     # Dependencies (langchain, streamlit, Pillow)
└── README.md            # Project Documentation