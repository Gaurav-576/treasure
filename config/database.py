from pymongo import MongoClient

client=MongoClient("mongodb+srv://gauravsingh96753:XLhZeXRCZUVXuXro@fastapi.e1lh6.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI")
db=client.treasure_hunt_2k25
collection_name=db["questions"]