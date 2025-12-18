from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class WeatherCrewai():
    """WeatherCrewai crew"""

    
    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def clothing_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['clothing_advisor'],
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
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )