import streamlit as st 
from langgraph_backend import chatbot 
from langchain_core.messages import HumanMessage 

# st.session -> dict -> 
CONFIG = {'configurable' : {'thread_id' : 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history of conversation between user and ai_assistant 
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# take the user input 
user_input = st.chat_input("Type here : ")

if user_input:
    # add user message to message history 
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # invoke chatbot to generate a response 
    response = chatbot.stream({'messages' : [HumanMessage(content=user_input)]}, config=CONFIG, stream_mode='messages')

    # add the messages to message history 
    # st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    ai_message = ""
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in response
        )
    
    # ai_message = response['messages'][-1].content 
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
