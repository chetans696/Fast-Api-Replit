from fastapi import APIRouter, Request
import google.generativeai as genai

ai = APIRouter()
GOOGLE_API_KEY = 'AIzaSyClAsekAgQN-88C46GunAQ3_PNyh__3Vvs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


@ai.get("/")
def inIt():
  return "AI is loaded and ready to use"


@ai.get("/ask-ai")
def ask_ai(request: Request):
  try:
    prompt = request.query_params.get("dd")
    print("Prompted by user: ", prompt)
    response = model.generate_content(prompt)
    print("response ==>>>>", response.text)
    return response.text
  except Exception as e:
    print("Error ==>>", e)
