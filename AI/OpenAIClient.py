import json
import pdb

from openai import OpenAI
from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Literal

client = OpenAI()

class Response(BaseModel):
    answer: str

class OpenAIClient:

    def send_message_ask_question(self, question, embedded_content) -> dict:
        systemContent = """
            You're a teacher helping college students.
            Answer the following question based only on the following context:
            {embedded_content}
            """
        question = question 
        apiMessages = [
            {"role": "system", "content": systemContent},
            {"role": "user", "content": question},
        ]
        
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=apiMessages,
            response_format=Response
        ) 
        print(completion)
        return completion.choices[0].message.parsed
    