# 🧠 AI Mental Health Therapist – *SafeSpace*  
---

## 🌟 Overview  
An **AI-powered virtual mental health assistant** built using **Google’s MedGemma LLM** and advanced chatbot frameworks.  
The project integrates **LLMs**, intelligent agents, and **emergency support tools** to provide safe, empathetic, and real-time mental health assistance.  


## 📸 Screenshots
C:\Users\priya\OneDrive\Pictures\Screenshots\Screenshot (1193).png
---

## ✨ Features  
- 🏥 **Healthcare-focused LLM** – Google MedGemma Family for medical context  
- 🔄 **Multi-LLM Support** – Ollama, GPT-4, Claude, Groq APIs  
- 🤖 **AI Chatbot Development** – LangChain, LangGraph, agentic workflows  
- 💻 **Frontend** – Built with Streamlit for a simple, intuitive UI  
- ⚡ **Backend** – FastAPI for scalable, fast request handling  
- 🛠 **AI Agent Tools**:  
  - 📞 Emergency calls via **Twilio**  
  - 📍 Location-based crisis assistance  
  - 👩‍⚕️ Professional mental health support integration  

---

## 🏗 Technical Architecture  
```plaintext
[Frontend: Streamlit]  <--->  [Backend: FastAPI]  <--->  [AI Agent Layer: MedGemma + Tools]
                                          |
                                 [Twilio / Location API]


---

## 🗂 Development Phases  
**Phase 1 – Frontend**  
✅ Streamlit interface setup  
✅ User queries → Backend connection  

**Phase 2 – Backend**  
✅ FastAPI API setup  
✅ Request validation & routing  

**Phase 3 – AI Agent & Tools**  
✅ Ollama + MedGemma integration  
✅ Twilio API for calls  
✅ Location services  
✅ AI Agent linked with backend  

**Phase 4 – Testing**  
✅ End-to-end testing & debugging  

---

## 🚀 Installation & Setup  
```bash
# Clone repository
git clone https://github.com/your-username/ai-therapist.git
cd ai-therapist

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload

# Run frontend
streamlit run app.py
