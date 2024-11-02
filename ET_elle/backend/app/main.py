
from fastapi import FastAPI, UploadFile, File, Form
from .agents import client, tech_lead_agent
import os

app = FastAPI()

@app.post("/process-file/")
async def process_file(file: UploadFile = File(None), file_path: str = Form(None)):
  if file:
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
      file_object.write(file.file.read())
  elif file_path:
    file_location = file_path
    if not os.path.exists(file_location):
      return {"error": "File path does not exist"}
  else:
    return {"error": "No file or file path provided"}

  # Trigger the Tech Lead Agent to process the file
  response = client.run(
    agent=tech_lead_agent,
    messages=[{"role": "user", "content": f"Process the file {file_location}"}],
  )

  return {"info": f"file '{file_location}' processed", "agent_response": response.messages[-1]["content"]}

