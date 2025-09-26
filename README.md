Intelligent Math & Knowledge Agent 🧠✨

An AI assistant powered by Groq and LangChain that can solve math problems and answer general knowledge questions by leveraging external tools to ensure accuracy and prevent hallucination.

➡️ View the Live Application Demo Here
https://sumit-1325-text-to-math-problem-solver----app-ay4bmx.streamlit.app/

🎯 The Problem
Standard Large Language Models (LLMs) are incredibly powerful but can sometimes "hallucinate" or generate incorrect information. This is especially true for tasks requiring precise, real-time data, such as mathematical calculations or factual queries about current events.
This project solves that problem by building a reasoning agent that uses specialized, reliable tools to find and verify information before providing an answer to the user.

✨ Key Features
 * Multi-Tool Agent: The AI agent intelligently decides which tool to use based on the user's query.
 * Accurate Math Solving: Integrates LangChain's LLMMathChain to perform precise mathematical calculations, avoiding LLM estimation errors.
 * Factual Lookups: Uses the Wikipedia API to fetch and summarize real-time, verifiable information for general knowledge questions.
 * Conversational Memory: Remembers the context of the conversation, allowing for natural, multi-turn follow-up questions.
 * High-Speed Inference: Powered by the gemma2-9b-it model running on the blazingly fast Groq LPU™ Inference Engine for a responsive, real-time experience.
 * Interactive UI: A clean and user-friendly chat interface built with Streamlit.
   
🛠️ Technical Architecture
The application is built around a LangChain Conversational Agent. This agent analyzes the user's prompt and makes a decision about the best tool to use for the task by following the ReAct (Reason and Act) framework.

 * Conversational Agent (CONVERSATIONAL_REACT_DESCRIPTION): The core of the application. It orchestrates the entire process, maintaining a thought-action-observation loop to reason about the problem.
   
 * Mathematical Grounding (LLMMathChain): For any query identified as a math problem, the agent uses this tool. It ensures that calculations are performed by a reliable Python numerical engine.
   
 * Factual Grounding (Wikipedia Tool): For general knowledge questions, the agent queries the Wikipedia API to fetch up-to-date information.
   
 * Memory
 * (ConversationBufferWindowMemory): The agent remembers the last few turns of the conversation, allowing it to understand the context of follow-up questions.
   
🚀 Tech Stack
 * AI Framework: LangChain
 * LLM & Inference: Google's gemma2-9b-it via Groq API
 * Frontend: Streamlit
 * Tools: LLMMathChain, Wikipedia API
 * Language: Python
⚙️ Setup and Local Installation
To run this project on your local machine, follow these steps:
 * Clone the Repository
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

 * Create a Virtual Environment (Recommended)
   python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

 * Install Dependencies
   pip install -r requirements.txt

 * Set Up Environment Variables
   * Create a file named .env in the root of the project directory.
     
   * Add your Groq API key to this file:
     GROQ_API_KEY="gsk_YourActualGroqApiKeyGoesHere"

 * Run the Streamlit App
   streamlit run app.py

   The application should now be running in your web browser!
     

🙏 Acknowledgements
This project was inspired by the excellent and comprehensive Generative AI course taught by @krishnaik06 His clear explanations of the LangChain ecosystem were invaluable in the development of this application.







