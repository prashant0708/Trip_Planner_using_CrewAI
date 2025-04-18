from crewai import Agent
import re
from crewai import LLM
from langchain_core.language_models.chat_models import BaseChatModel
from tools.browser_tools import BrowserTools
from tools.calculate_tools import CalculatorTools
from tools.search_tools import SearchTools

class TripAgents():
    def __init__(self,llm:BaseChatModel=None):
        if llm is None:
            self.llm =  LLM(model="gemini/gemini-2.0-flash")
        else:
            self.llm = llm
            
        ## Intilize the tools 
        
        self.search_tool = SearchTools()
        self.browser_tool = BrowserTools()
        self.calculator_tool = CalculatorTools()
        
    def city_selection_agent(self):
        return Agent(
            role = 'City Selection Expert',
            goal = 'Select the best city based on weather , season and prices',
            backstory='An Experts to analyze the travel data to pick ideal destination',
            tools = [self.search_tool,self.browser_tool],
            allow_delegation=False,
            llm = self.llm,
            verbose= True
        )
        
    def local_expert(self):
        return Agent(
            role = 'Local Expert at the city',
            goal = 'Provide the best insight about the city',
            backstory='An Experts local guide with extensive information about the city , which help customer to know about the city',
            tools = [self.search_tool,self.browser_tool],
            allow_delegation=False,
            llm = self.llm,
            verbose= True
        )
        
    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[self.search_tool, self.browser_tool, self.calculator_tool],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
        