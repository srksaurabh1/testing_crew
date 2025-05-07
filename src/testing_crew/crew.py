from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict

@CrewBase
class TestingCrew():
    """TestingCrew crew"""
    
    agents_config: Dict[str, dict]
    tasks_config: Dict[str, dict]
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], 
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
            agent=self.researcher()
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], 
            agent=self.reporting_analyst(), 
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TestingCrew crew"""
        if not self.agents:
            self.agents = [self.researcher(), self.reporting_analyst()]

        if not self.tasks:
            self.tasks = [self.research_task(), self.reporting_task()]

        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )