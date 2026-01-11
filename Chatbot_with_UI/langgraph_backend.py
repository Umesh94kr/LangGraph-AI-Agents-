from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated 
from langchain_core.messages import HumanMessage, BaseMessage 
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama 
from langgraph.graph.message import add_messages # adding a reducer function 
from langgraph.checkpoint.memory import InMemorySaver

############ LLM used #############
llm = ChatOllama(
    model='llama3.2',
    verbose=True,
    temperature=0.2
)

########## State of Graph ##########
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages] 

########## Nodes function #####
def chat_llm(state: ChatState) -> ChatState:
    template = """ 
                You are a helpful chatbot, which takes user query and history of messages and returns an output.Do not output anything rubbish just a short conversational response.
                <query + history> {messages} </query + history> 
               """

    prompt = PromptTemplate(
        template=template,
        input_variables=['messages']
    )

    chain = prompt | llm 
    response = chain.invoke({'messages' : state['messages']})
    return {
        'messages' : [response]
    }

########## Create a Graph ##########
graph = StateGraph(ChatState)

# adding nodes 
graph.add_node('chat_llm', chat_llm)

# add edges to graph 
graph.add_edge(START, 'chat_llm')
graph.add_edge('chat_llm', END)

# configs 
checkpointer = InMemorySaver()

# compile graph 
chatbot = graph.compile(checkpointer=checkpointer)

