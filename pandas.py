import os
import json
import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
import pandas as pd

os.environ["OPENAI_API_KEY"] = "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"

df = pd.read_csv("titanic.csv")

# Create the agent
agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# Set the title of the app
st.title("Chatbot")

# Function to display messages in a conversational format
def show_messages(messages):
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.text_input("User:", value=content, key=content, disabled=True)
        elif role == "system":
            st.text_area("Agent:", value=content, key=content, disabled=True)

st.session_state.setdefault("messages", [])

prompt = st.text_input("User:", "")

if prompt:
    with st.spinner("Generating response..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        prompt_json = json.dumps(prompt)
        response = agent.run(prompt_json)
        message_response = response
        st.session_state["messages"] += [
            {"role": "system", "content": message_response}
        ]
        show_messages(st.session_state["messages"])
