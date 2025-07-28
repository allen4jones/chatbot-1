import streamlit as st
# import requests  # Keep this for later use when real backend is ready

# Mock endpoint (replace with real one later)
# BACKEND_URL = "https://your-real-backend.com/chat"

st.set_page_config(page_title="Seed Law Chatbot", page_icon="🌱")
st.title("🌱 Chat with Phi-4 Mini")
st.caption("Frontend only – backend is mocked for now.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Chat input box
if prompt := st.chat_input("Ask a question about seed laws..."):
    st.session_state.chat_history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # === MOCKED BACKEND RESPONSE ===
    # When you're ready, uncomment the request below and delete this mock section
    #
    # try:
    #     response = requests.post(BACKEND_URL, json={"question": prompt})
    #     answer = response.json()["answer"]
    # except Exception as e:
    #     answer = f"⚠️ Error contacting backend: {e}"

    # Temporary fake reply
    mock_responses = {
        "what are seed laws": "Seed laws are regulations that govern the quality, labeling, and distribution of seeds to ensure agricultural standards.",
        "who enforces seed laws": "Seed laws are enforced by agricultural departments or seed regulatory agencies in each country.",
    }
    answer = mock_responses.get(prompt.lower(), "This is a mock response. Your question will be answered by the real model once connected.")

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.chat_history.append(("assistant", answer))

