import streamlit as st
from scripts.guess_agents import gambler, player
import torch
import gc

# Game logic function
def start_conversation(message="Tell me the rules, I am ready!", turns=6):
    sender = player
    receiver = gambler
    for i in range(turns):
        with st.spinner(f"Turn {i+1} in progress..."):
            sender.send(recipient=receiver, message=message)
            result = receiver.generate_reply(sender=sender, messages=None)
            message = result["content"]
            sender, receiver = receiver, sender
            yield result

# Sidebar settings
st.sidebar.title("🎮 Game Settings")
num_turns = st.sidebar.slider("Number of Turns", min_value=1, max_value=10, value=6)
start_message = st.sidebar.text_input("Starting Message", value="Tell me the rules, I am ready!")

# Main UI
st.title("🤖 AutoGen Guessing Game")
st.markdown("Welcome to the **AutoGen Demo**. Watch the agents play a guessing game with each other.")

st.divider()
st.chat_message("admin").write("🎲 Game ON!")

# Run the conversation
for result in start_conversation(message=start_message, turns=num_turns):
    st.chat_message(result["role"]).write(result["content"])

# Memory cleanup
torch.cuda.empty_cache()
gc.collect()

st.success("Game finished! 🏁")
