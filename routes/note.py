from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from openai import OpenAI

note = APIRouter()
templates = Jinja2Templates(directory="templates")

client = OpenAI(
    api_key='sk-proj-KSJDVfrKhBjidVVVo7KYT3BlbkFJgEYUTLMgCKzZYx3n3ZhF')
# openai.api_key = 'sk-proj-JX3YVRE2s7ZTnMbhcj9WT3BlbkFJvX0AiZZV6TwEhSba4K6L'
# api_key='sk-proj-bJUpcx83iKf2n3CFm6teT3BlbkFJOFMvJY01UKY59zDgx7tW'


@note.get("/")
async def getUsers():
    users = conn.sample_mflix.users.find({}).limit(10)

    allUsers = []
    for user in users:
        allUsers.append({"name": user["name"], "email": user["email"]})
    return allUsers


@note.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(request=request,
                                      name="index.html",
                                      context={"id": id})


# Function to get a response from ChatGPT
@note.get("/chatgpt")
async def get_chatgpt_response():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "system",
            "content":
            "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
        }, {
            "role":
            "user",
            "content":
            "Compose a poem that explains the concept of recursion in programming."
        }])

    print(completion.choices[0].message)
    return completion.choices[0].message
