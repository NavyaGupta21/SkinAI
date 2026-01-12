# ✨ SkinAI: Personalized Skincare Consultant

![Status](https://img.shields.io/badge/Status-Live-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.41-FF4B4B) ![LangChain](https://img.shields.io/badge/Framework-LangChain-green)

**SkinAI** is an AI-powered multimodal web application. It acts as a virtual skincare consultant by using **Google Gemini 1.5 Flash** integrated via **LangChain** to analyze facial images and provide data-driven skincare advice.

## 🧐 Problem Statement
The skincare market is overwhelmed with products, causing "analysis paralysis." Consumers often misidentify their skin type, leading to incorrect product usage. SkinAI provides a fast, science-based starting point for a personalized skincare journey.

## 🚀 Key Features
* **📸 Multimodal Vision Scan:** Analyzes facial images to identify skin type, Fitzpatrick scale, and concerns.
* **💬 Context-Aware Chat:** Remembers the initial analysis report during follow-up questions using **LangChain's Stateful Logic**.
* **⚡ Optimized Processing:** Images are resized to **512x512** for faster API calls and lower latency.
* **🛡️ Professional Formatting:** Outputs analysis in clean Markdown tables for high readability.

## 🛠️ How It Works (The Logic)
1. **Image Encoding:** The app uses `Pillow` to resize and convert images to Base64, ensuring they are small enough for fast transmission to Gemini.
2. **Analysis:** A specialized "Dermatologist Prompt" forces the AI to output a structured report (Type, Routine, Actives).
3. **Memory Management:** For the chat, the app uses a **Context Injection** strategy where the initial report is "pinned" as an `AIMessage` so the chatbot never forgets the original scan.

## 🧠 Technology Stack
| Component | Technology Used |
| :--- | :--- |
| **Frontend/UI** | Streamlit (1.41.1) |
| **Orchestration** | LangChain Core |
| **AI Model** | Gemini 1.5 Flash |
| **Image Processing** | Pillow (PIL) |

## 📂 Installation
1. Clone the repo.
2. Add your `GOOGLE_API_KEY` to `.streamlit/secrets.toml`.
3. Run `pip install -r requirements.txt`.
4. Launch with `streamlit run Skincare.py`.