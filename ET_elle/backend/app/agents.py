
from swarm import Swarm, Agent
from .csv_processing import read_csv_sample

client = Swarm()

def delegate_to_schema_management(file_location):
  sample_data = read_csv_sample(file_location)
  response = schema_management_agent.run(messages=[{"role": "system", "content": f"Sample data: {sample_data}"}])
  return handle_agent_response(response, "Schema Management")

def delegate_to_query_planning(file_location):
  sample_data = read_csv_sample(file_location)
  response = query_planning_agent.run(messages=[{"role": "system", "content": f"Sample data: {sample_data}"}])
  return handle_agent_response(response, "Query Planning")

def handle_agent_response(response, agent_name):
  print(f"{agent_name} Agent Response: {response.messages[-1]['content']}")
  if "clarification needed" in response.messages[-1]['content']:
    return tech_lead_agent
  return None

tech_lead_agent = Agent(
  name="Tech Lead Agent",
  instructions="Delegate tasks to specialized agents and handle their feedback.",
  functions=[
    delegate_to_schema_management,
    delegate_to_query_planning
  ],
)

schema_management_agent = Agent(
  name="Schema Management Agent",
  instructions="Propose data schema and optimize workflows for incoming data.",
)

query_planning_agent = Agent(
  name="Query Planning Agent",
  instructions="Use sample data and row counts to suggest optimal execution plans.",
)

# Example of running the Tech Lead Agent
response = client.run(
  agent=tech_lead_agent,
  messages=[{"role": "user", "content": "Start processing tasks for the new CSV file."}],
)

print(response.messages[-1]["content"])

