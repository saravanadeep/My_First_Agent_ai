#Importing the agent from the google adk agent kit.
from google.adk.agents.llm_agent import Agent

#Declaring imported agent to root_agent.
root_agent = Agent(

    #model name of the agent.
    model='gemini-2.5-flash',

    #Name of the agent.
    name='root_agent',

    #Description of the agent.
    description='A helpful assistant for user questions.',

    #Giving instruction to the agent.
    instruction='Answer user questions to the best of your knowledge',
)
