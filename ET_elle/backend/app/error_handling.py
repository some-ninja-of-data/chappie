
def safe_run(agent, message):
  try:
    response = agent.run(messages=[{"role": "user", "content": message}])
    return response
  except Exception as e:
    print(f"Error in {agent.name}: {e}")
    # Implement retry logic or log the error
    return None

