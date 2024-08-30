from pydantic import BaseModel

class Question(BaseModel):
  question: str
  image: str
  spotname: str
  spotId: str
  code: str
  scanner: bool