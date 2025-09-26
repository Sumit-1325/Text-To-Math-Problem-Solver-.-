import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv

# --- Helper Function to Load CSS ---
def load_css(file_path):
    """Loads a CSS file and injects it into the Streamlit app."""
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found at {file_path}. Please check the path.")

# --- Main Application ---
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="Intelligent Math & Knowledge Agent",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Load the external CSS file
load_css("style.css")

st.title("Intelligent Math & Knowledge Agent")
st.caption("🚀 An AI assistant powered by Groq and LangChain, capable of solving math problems and searching Wikipedia.")
st.divider()

# --- Initialize session state for memory ---
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        k=5, # Remembers the last 5 conversation exchanges
        memory_key="chat_history", 
        return_messages=True
    )

try:
    llm = ChatGroq(
        temperature=0,
        model="gemma2-9b-it",
        api_key=groq_api_key
    )
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    math_tool = Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="Useful for when you need to answer questions about math. Input should be a single numerical or mathematical expression.",
    )
    wikipedia = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for when you need to answer general knowledge questions or look up information about people, places, or concepts. Input should be a search query string.",
    )
    tools = [math_tool, wikipedia_tool]
    
    agent_executor = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=st.session_state.memory,
        return_intermediate_steps=True, # Explicitly ask for intermediate steps
        verbose=True
    )
except Exception as e:
    st.error(f"Failed to initialize the AI agent. Please check your GROQ_API_KEY. Error: {e}")
    st.stop()

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hello! How can I assist you today with math or general knowledge?"})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a math problem or a knowledge question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            with st.expander("Agent's Thought Process", expanded=True):
                # Use agent_executor.invoke and manually display intermediate steps
                response_dict = agent_executor.invoke({"input": prompt})
                
                intermediate_steps = response_dict.get("intermediate_steps", [])
                
                for i, step in enumerate(intermediate_steps):
                    action, observation = step
                    st.subheader(f"Step {i+1}: Tool Action")
                    st.markdown(f"**Action:** `{action.tool}`")
                    st.markdown(f"**Action Input:** `{action.tool_input}`")
                    st.markdown(f"**Log:**\n```\n{action.log.strip()}\n```")
                    st.subheader(f"Step {i+1}: Observation")
                    st.markdown(f"```\n{observation}\n```")
                    st.divider()

                full_response = response_dict.get("output", "No output found.")
        except Exception as e:
            full_response = f"Sorry, I encountered an error: {e}"
            st.error(full_response)
        
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

