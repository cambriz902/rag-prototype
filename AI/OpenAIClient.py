import json
import pdb

from openai import OpenAI
from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Literal
# from ..serializer import MealSerializer

client = OpenAI()

class Response(BaseModel):
    answer: str

class OpenAIClient:

    def send_message(self, messages, embedded_content) -> dict:
        systemContent = """""" 
        apiMessages = [
            {"role": "system", "content": systemContent},
            {"role": "user", "content": ""},
        ]
        
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=apiMessages,
            response_format=Response
        ) 
        return completion.choices[0].message.parsed
    