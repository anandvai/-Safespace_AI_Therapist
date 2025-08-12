# step 1 : Setup Streamlit for frontend 
import streamlit as st,requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title = "AI Mental Health Therapist", layout = "wide")
st.title("🧠 SafeSpace - AI Mental Health Therapist")

#initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# step2: user is able to ask question 
user_input = st.chat_input("What's on your mind today?")
if user_input:
    #Append user message 
    st.session_state.chat_history.append({"role": "user" , "content": user_input})

    #AI Agent exists here 
    response = requests.post(BACKEND_URL, json={"message": user_input})

    #st.session_state.chat_history.append({"role": "assistant", "content": response.json()})

    st.session_state.chat_history.append({"role": "assistant", "content": f'{response.json()["response"]}WITH TOOL: [{response.json()["tool_called"]}]'})

    #step3 : Show response from backend
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


