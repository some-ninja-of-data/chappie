
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
  if credentials.username != "user" or credentials.password != "pass":
    raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/secure-endpoint")
def secure_endpoint(credentials: HTTPBasicCredentials = Depends(authenticate)):
  return {"message": "Secure data"}

