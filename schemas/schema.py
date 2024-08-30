def individual_serial(question) -> dict:
  return {
    "id": str(question["_id"]),
    "question": question["question"],
    "image": question["image"],
    "spotname": question["spotname"],
    "spotId": question["spotId"],
    "code": question["code"],
    "scanner": question["scanner"]
  }
  
def list_serial(questions) -> list:
  return [individual_serial(question) for question in questions]