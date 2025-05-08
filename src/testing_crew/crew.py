from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict
import yaml
from crewai_tools import SerperDevTool

@CrewBase
class TestingCrew():
    def __init__(self):
        self.llmGemini = LLM(model="gemini/gemini-1.5-flash",
                       temperature=0.7,)   
            
        self.agents_config: Dict[str, dict]
        self.tasks_config: Dict[str, dict]
        self.agents: List[BaseAgent]
        self.tasks: List[Task]
        
        filepath="src/testing_crew/config/config.yaml"
        with open(filepath, 'r') as f:
            config = yaml.safe_load(f)
        
        self.company_name = config['company_name']
        self.tool_google_search = SerperDevTool(
            name=self.company_name,
            n_results=3
        )

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs # You can return the inputs or modify them as needed

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            verbose=True, 
            llm=self.llmGemini,
            tools=[self.tool_google_search])

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], 
            verbose=True,
            llm=self.llmGemini,
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
            verbose=True)
            
    @after_kickoff
    def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result # You can return the result or modify it as needed
        