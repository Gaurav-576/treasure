from bson import ObjectId
from fastapi import FastAPI
from config.database import collection_name
from schemas.schema import list_serial
from models.questions import Question
from fastapi.openapi.docs import get_swagger_ui_html

app=FastAPI()

@app.get("/", include_in_schema=False)
async def redirect_to_swagger():
  return get_swagger_ui_html(openapi_url=app.openapi_url, title="Swagger UI")

@app.post("/questions/")
async def create(question: Question):
  collection_name.insert_one(dict(question))
  return "Question added successfully"

@app.get("/questions/")
async def read():
  questions=collection_name.find()
  return list_serial(list(questions))

@app.put("/questions/{id}")
async def update(id: str,question: Question):
  collection_name.find_one_and_update({"_id": question(id)}, {"$set": dict(question)})
  return "Question with name: {question} updated successfully"
  
@app.delete("/questions/{id}")
async def delete(id: str):
  collection_name.find_one_and_delete({"_id": ObjectId(id)})
  return f"Question with id: {id} deleted successfully"
