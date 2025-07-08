# 🥗 Smartest AI Nutrition Assistant

**Smartest AI Nutrition Assistant** is an innovative, AI-powered web application developed as a capstone team project during the **Artificial Intelligence Powered Assistant (AIPA)** course at **National Skill Training Institute (Women), Indore**.  
This course is offered by the **Directorate General of Training (DGT)** in collaboration with **Microsoft** and the **Edunet Foundation** under the **Future Ready Talent** initiative.

---

## 📌 Project Objective

The goal of this project is to create a smart, user-friendly chatbot that provides **personalized nutrition recommendations** based on individual health goals such as weight gain, weight loss, or maintaining fitness. It leverages **Generative AI** to process multiple input types (text, voice, and image) and deliver relevant, adaptive suggestions.

---

## 🚀 Key Features

- 🧠 **AI-Driven Chatbot**: Built using OpenRouter (OpenAI) API to provide smart, human-like responses.
- 📋 **Personalized Meal Planning**: Customized daily plans based on user goals.
- 🔁 **Feedback Learning Loop**: Learns from user feedback to fine-tune suggestions.
- 🎙️ **Voice Input Support**: Allows interaction via speech (where applicable).
- 📸 **Image Input Integration** *(planned)*: Future extension for food image analysis.
- 🧾 **Nutrition and Calorie Breakdown**: Shows estimated daily intake and suggestions.
- 🖥️ **Interactive UI**: Designed with Streamlit for a clean and intuitive experience.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: Python, OpenAI API via OpenRouter
- **Environment Variables**: `.env` for secure API key storage
- **Other Tools**: dotenv, requests, base64, PIL for media handling

---

## 👩‍💻 Team Members

| Name |
| Gagandeep Kaur Rajpal|
| Shivanee Pawar|
| Surbhi Sharma |
| Anjali Garothiya |
| Sharmila Bhawel |

---

## 📁 Project Structure
Smartest-AI-Nutrition-Assistant/
│
├── app.py # Main Streamlit app
├── requirements.txt 
├── .env # API key 
├── assets
├── utils
└── README.md 


---

## 🎯 Future Enhancements
🧬 Integration of BMI and health parameter inputs

📸 Image-based food recognition

📊 Data storage and user progress tracking

📱 Deployment as a mobile app

🌐 Multilingual chatbot responses

---

## 📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it for educational and non-commercial purposes.

---

## 🙌 Acknowledgements
DGT, Ministry of Skill Development and Entrepreneurship (MSDE), India

Microsoft for providing cloud & AI services

Edunet Foundation for organizing and supporting the AIPA course

All mentors and instructors who guided us during the course

"Fuel your health with intelligence. Let AI serve your plate with purpose."

---

## 🔧 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/GagandeepKaur07/Smartest-AI-Nutrition-Assistant.git
cd Smartest-AI-Nutrition-Assistant

pip install -r requirements.txt

Create a .env file in the root directory with:
OPENROUTER_API_KEY=your_openrouter_api_key_here

streamlit run app.py

