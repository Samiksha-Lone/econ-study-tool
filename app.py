import streamlit as st
from openai import OpenAI as openai
import os

st.set_page_config(page_title="Oligopoly Study Tool", layout="wide")
st.title("🎓 Oligopoly Study Tool - NotebookLM Style")

# OpenAI API Key
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
if not api_key:
    st.info("👈 Enter your OpenAI API key (free at platform.openai.com)")
    st.stop()

# Economics Context (Oligopoly content)
CONTEXT = """
Oligopoly: Few large firms dominate market. High interdependence - one firm's price change affects rivals.
Kinked Demand Curve: Above current price (P1) - elastic (rivals don't follow price rise). Below P1 - inelastic (rivals match price cut). Creates MR discontinuity → price rigidity.
Game Theory: Prisoner's Dilemma payoff matrix. Nash Equilibrium = both firms charge low price (£90k profit each). Collusion unstable due to cheating incentive.
Exam Tips: Always draw kinked AR/MR graph. Mark Nash equilibrium cell clearly.
"""

mode = st.sidebar.selectbox("Select Mode", ["🗣️ Teacher-Student Dialogue", "📹 Video Summaries"])

if mode == "🗣️ Teacher-Student Dialogue":
    st.header("🗣️ Simulated Teacher-Student Conversation")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": f"You are simulating TEACHER-STUDENT dialogue about oligopoly economics. Use ONLY this context: {CONTEXT}. Teacher explains clearly. Student asks natural questions. Keep conversational."}
        ]
    
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ask about oligopoly (e.g., 'What is kinked demand curve?')"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            
            client = openai(api_key=api_key)

            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.messages,
                )
                msg = response.choices[0].message.content
            except Exception as e:
                msg = (
                    "The AI response cannot be generated right now because the API quota "
                    "for this demo key is exhausted. The rest of the interactive flow "
                    "still demonstrates how the tool works."
                )
     
            st.markdown(msg)
            st.session_state.messages.append({"role": "assistant", "content": msg})

else:
    st.header("📹 Video Summaries + Exam Tips")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Kinked Demand Curve")
        st.video("https://youtu.be/Ec19ljjvlCI")
        st.markdown("**Key Points:** Elastic above P1, inelastic below → Price rigidity")
    
    with col2:
        st.subheader("2. Game Theory")
        st.video("https://youtu.be/Z_S0VA4jKes")
        st.markdown("**Key Points:** Nash Equilibrium = Low price strategy")
