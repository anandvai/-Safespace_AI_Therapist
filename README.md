# 🧠 AI Mental Health Therapist – *SafeSpace*  
---

## 🌟 Overview  
An **AI-powered virtual mental health assistant** built using **Google’s MedGemma LLM** and advanced chatbot frameworks.  
The project integrates **LLMs**, intelligent agents, and **emergency support tools** to provide safe, empathetic, and real-time mental health assistance.  


## 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot (1193)" src="https://github.com/user-attachments/assets/c118f382-1b2e-40b7-a877-1b00dc91b9f4" />

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
## 🔍 How It Works  

The AI Mental Health Therapist follows a simple yet powerful workflow to assist users in real time:

1. **User Interaction (Frontend – Streamlit)**  
   - The user opens the Streamlit web interface and starts a conversation.  
   - Messages are typed into the chat box or spoken through voice input (if enabled).  

2. **Request Handling (Backend – FastAPI)**  
   - The frontend sends the user’s query to the FastAPI backend.  
   - The backend validates the input for safety, context, and completeness.  

3. **AI Processing (MedGemma + LLMs)**  
   - The backend forwards the query to the **AI Agent**, powered by Google’s **MedGemma LLM**.  
   - Depending on the request, additional models (Ollama, GPT-4, Claude, Groq) may be used for reasoning or empathy enhancement.  

4. **Tool Activation (Agentic Workflow)**  
   - If the AI detects a crisis or emergency:
     - **📞 Twilio API** triggers an emergency call to a pre-defined contact or helpline.  
     - **📍 Location Service** fetches the user’s location for emergency assistance.  
     - **👩‍⚕️ Professional Support** information is provided.  

5. **Response Delivery**  
   - The AI generates a compassionate, context-aware response.  
   - The backend sends the final answer back to the Streamlit frontend for display.  

6. **Continuous Conversation**  
   - The session remains active for follow-up questions, maintaining conversational context.  

**In short:**  
User → **Streamlit** → **FastAPI** → **MedGemma + Tools** → Response + Optional Emergency Support

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
