import streamlit as st
from openai import OpenAI
from openai import AzureOpenAI

st.title("Chatbot")

openai_api_key = st.secrets["AZURE_OPENAI_API_KEY"]
openai_api_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]

client = AzureOpenAI(
    api_key=openai_api_key,
    api_version="2024-12-01-preview",
    azure_endpoint=openai_api_endpoint
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about anyone on the list"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    stream = client.chat.completions.create(
        model=st.secrets["AZURE_OPENAI_MODEL"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )

    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
