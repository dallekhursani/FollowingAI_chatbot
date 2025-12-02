from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_llm_response(conversation):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation
    )
    return response.choices[0].message["content"]
