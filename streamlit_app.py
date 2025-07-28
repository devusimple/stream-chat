import streamlit as st

st.set_page_config(page_title="Messaging App", layout="wide")

st.title("💬 Messaging Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat history display
st.markdown("### Chat History")
for msg in st.session_state["messages"]:
    st.write(f"**{msg['user']}**: {msg['text']}")

# Message input
with st.form("message_form", clear_on_submit=True):
    user = st.text_input("Your name", value="User")
    text = st.text_input("Type your message")
    submitted = st.form_submit_button("Send")
    if submitted and text:
        st.session_state["messages"].append({"user": user, "text": text})
        st.experimental_rerun()

st.markdown("---")
st.markdown("Built with [Streamlit](https://streamlit.io/)")