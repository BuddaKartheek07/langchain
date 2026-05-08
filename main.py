from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
load_dotenv() 





llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()] 
agent = create_agent(model=llm, tools=tools) 


def main():
    print("Hello from langchain!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postingss for an ai engineer using langchain in the bay area on linkedin and list their details")}) 
    print(result) 

if __name__ == "__main__":
    main() 
