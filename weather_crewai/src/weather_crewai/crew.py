import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from typing import List

@CrewBase
class WeatherCrewai():
    """WeatherCrewai crew"""

    # 1. Initialize the Search Tool
    # Note: Ensure os.environ["SERPER_API_KEY"] is set in your Colab notebook
    search_tool = SerperDevTool()

    # 2. Define your Ollama LLM for Mistral
    # base_url is typically http://localhost:11434 on Colab 
    # if you are running Ollama in the background.
    mistral_llm = LLM(
        model="ollama/mistral",
        base_url="http://localhost:11434"
    )

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[self.search_tool], # Added the tool here
            llm=self.mistral_llm,      # Using Mistral
            verbose=True
        )

    @agent
    def clothing_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['clothing_advisor'],
            llm=self.mistral_llm,      # Using Mistral
            verbose=True
        )

    @task
    def weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_task'],
        )

    @task
    def clothing_task(self) -> Task:
        return Task(
            config=self.tasks_config['clothing_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )