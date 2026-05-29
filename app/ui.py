import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Import assistants
from assistants.oss_assistant import OSSAssistant
from assistants.frontier_assistant import FrontierAssistant

# Import safety checker
from utils.safety import is_safe

# ---------------------------------------------------
# Streamlit page configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="DualMind AI",
    page_icon="",
    layout="wide"
)

# ---------------------------------------------------
# Page title
# ---------------------------------------------------
st.title("DualMind AI")

st.markdown("""
Compare:
- Open Source Assistant
- Frontier Model Assistant
""")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.header("Settings")

assistant_type = st.sidebar.selectbox(
    "Choose Assistant",
    [
        "OSS Assistant",
        "Frontier Assistant"
    ]
)

# ---------------------------------------------------
# Initialize assistants only once
# ---------------------------------------------------
if "oss_assistant" not in st.session_state:

    # Store OSS assistant object
    st.session_state.oss_assistant = OSSAssistant()

if "frontier_assistant" not in st.session_state:

    # Store Frontier assistant object
    st.session_state.frontier_assistant = FrontierAssistant()

# ---------------------------------------------------
# Store chat history in Streamlit session
# ---------------------------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = []

# ---------------------------------------------------
# Display old messages
# ---------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------------------------
# Chat input box
# ---------------------------------------------------
user_input = st.chat_input("Type your message here...")

# ---------------------------------------------------
# When user sends message
# ---------------------------------------------------
if user_input:

    # -----------------------------
    # Safety Check
    # -----------------------------
    if not is_safe(user_input):

        st.error("⚠ Unsafe prompt detected.")

        st.stop()

    # -----------------------------
    # Save user message
    # -----------------------------
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Show user message
    with st.chat_message("user"):

        st.markdown(user_input)

    # -----------------------------
    # Generate assistant response
    # -----------------------------
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Select assistant
            if assistant_type == "OSS Assistant":

                response = st.session_state.oss_assistant.chat(
                    user_input
                )

            else:

                response = st.session_state.frontier_assistant.chat(
                    user_input
                )

            # Display response
            st.markdown(response)

    # -----------------------------
    # Save assistant response
    # -----------------------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.sidebar.markdown("---")

st.sidebar.info("""
Project Features:
- Multi-turn memory
- OSS vs Frontier comparison
- Safety filtering
- Evaluation ready
""")