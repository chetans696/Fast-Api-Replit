from fastapi import APIRouter
import google.generativeai as genai
from pydantic import BaseModel
import random
import textwrap
from IPython.display import Markdown

ai = APIRouter()
GOOGLE_API_KEY = 'AIzaSyClAsekAgQN-88C46GunAQ3_PNyh__3Vvs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


class Query(BaseModel):
  ques: str


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


@ai.get("/")
def inIt():
  return "AI is loaded and ready to use"


@ai.post("/ask-ai")
def ask_ai(query: Query):
  try:
    print("Prompted by user: ", query.ques)
    response = model.generate_content(query.ques or "hi")
    print("response ==>>>>", response)
    finish_reason = response.candidates[0].finish_reason
    text = response.text if finish_reason == 1 else "Unable to generate response! Please try again."
    output = {"role": "AI", "response": to_markdown(text), "text": text}
    return output
  except Exception as e:
    print("Error ==>>", e)
