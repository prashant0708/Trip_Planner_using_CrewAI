import json
import requests
import streamlit as st
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from unstructured.partition.html import partition_html
from crewai import Agent, Task
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from crewai import LLM

class WebsiteInput(BaseModel):
    url: str = Field(..., description="The URL of the website to scrape")

class BrowserTools(BaseModel):
    name:str = "Scrape website content"
    description :str = "Proficient to scrape and summarize a website content"
    details : type[BaseModel] =WebsiteInput
    
    def run(self,website:str) ->str:
        try:
            url = f"https://chrome.browserless.io/content?token={st.secrets['BROWSERLESS_API_KEY']}"
            
            payload = json.dump({"url":website})
            
            headers = {'cache-control':'no-cache','content-type':'application/json'}
            
            response = requests.request("POST",headers=headers,url=url,data=payload)
            
            if response.status_code!=200:
                return f"Error:Failed to fetch website content State code : {response.status_code}"
            
            elements = partition_html(text=response.text)
            
            content = '\n\n'.join([str(text) for text in elements])
            print(f"This is the content from the Browsing tools{content}")
            summaries = []
            
            llm = LLM(model="gemini/gemini-2.0-flash")
            
            for chunk in content:
                agent = Agent(
                    role= 'Principal Researcher'
                    goal = 'Do amazing researches and summaries based on the content you are working with',
                    backstory= "ou're a Principal Researcher at a big company and you need to do a research about a given topic.",
                    allow_delegation=False
                    llm=llm
                )          
                
                task = Task(
                    description=f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}',
                    agent=agent
                )   
                summery = task.execute()
                summaries.append(summery)
            return "\n\n".join(summaries)
        
        except Exception as e:
            return f"Error while processing website: {str(e)}"
                