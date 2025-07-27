import streamlit as st
import requests

# Set your DeepSeek API Key here
DEEPSEEK_API_KEY = "sk-677d17ccd0ab4fcc8196f0f561299c0a"

# Function to query DeepSeek API
def ask_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Streamlit UI
def main():
    st.title("DeepSeek AI Chatbot")
    
    # Chat history container
    chat_history = st.container()
    user_input = st.text_input("You:", "")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    if user_input:
        # Add user message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get AI response
        ai_response = ask_deepseek(user_input)
        
        # Add AI response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**AI:** {message['content']}")

if __name__ == "__main__":
    main()