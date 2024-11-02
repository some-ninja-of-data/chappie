
from app.agents import tech_lead_agent
from app.error_handling import safe_run

def test_agent_response():
  response = safe_run(tech_lead_agent, "Test message")
  assert response is not None
  assert "expected content" in response.messages[-1]["content"]

