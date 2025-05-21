from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import SearchAndContents, FindSimilar, GetContents
from langchain_groq import ChatGroq
from datetime import datetime
from langchain_core.agents import AgentFinish
import json
import os
import time
#os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API')

@CrewBase
class NewsletterGenCrew:
    """NewsletterGen crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def llm(self):
        llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="groq/llama-3.3-70b-versatile")
        #llm = LLM(api_key=os.getenv('GROQ_API_KEY'), model='groq/meta-llama/llama-4-scout-17b-16e-instruct')
        return llm

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SearchAndContents()],
            verbose=False,
            allow_delegation=False,
            llm=self.llm()
            #step_callback=lambda step: self.step_callback(step, "Research Agent")
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            verbose=False,
            allow_delegation=False,
            llm=self.llm()
            #step_callback=lambda step: self.step_callback(step, "Chief Editor")
        )

    @agent
    def designer(self) -> Agent:
        return Agent(
            config=self.agents_config["designer"],
            verbose=False,
            allow_delegation=False,
            llm=self.llm()
            #step_callback=lambda step: self.step_callback(step, "HTML Writer")
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher()
        )
 
    @task
    def edit_task(self) -> Task:
        return Task(
            config=self.tasks_config["edit_task"],
            agent=self.editor()
        )

    @task
    def newsletter_task(self) -> Task:
    # Define the task
        return Task(
            config=self.tasks_config["newsletter_task"],
            agent=self.designer(),
            #output_file=output_file
        )
           
    @crew
    def crew(self) -> Crew:
        """Creates the NewsletterGen crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
