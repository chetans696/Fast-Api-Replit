from fastapi import APIRouter
import google.generativeai as genai
from pydantic import BaseModel
import random

ai = APIRouter()
GOOGLE_API_KEY = 'AIzaSyClAsekAgQN-88C46GunAQ3_PNyh__3Vvs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


class Query(BaseModel):
  ques: str


@ai.get("/")
def inIt():
  return "AI is loaded and ready to use"


@ai.post("/ask-ai")
def ask_ai(query: Query):
  try:
    print("Prompted by user: ", query.ques)
    response = model.generate_content(query.ques or "hi")
    print("response ==>>>>", response)
    output = {
      "id": random.randint(1000, 9999),
      "AI": response.text
    }
    return output
  except Exception as e:
    print("Error ==>>", e)
