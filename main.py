from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient
load_dotenv() 

tavily = TavilyClient() 

@tool
def brave_search(query: str)-> str:
    """
    
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """

    print(f"Searching for {query}") 
    return tavily.search(query=query) 


llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
tools = [brave_search]
agent = create_agent(model=llm, tools=tools) 

def main():
    print("Hello from langchain!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postingss for an ai engineer using langchain in the bay area on linkedin and list their details")}) 
    print(result) 

if __name__ == "__main__":
    main() 
