
from openai import OpenAI
from services.parse_schema import ATS_Response
import os
import json

class Openai_Service:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def get_openai_response(self, images):
        response = self.client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": 'Suppose you are a ATS tool. You have to parse resume/cv is a structured format, e.g.: { "name": "John Doe", "email": "johndoe@example.com", "skills": ["Python", "Machine Learning"] }. You will be given image or sets of images of one resume. If there multiple image, consider all of them from the same resume.',
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image
                        }
                    } for image in images
                ]
            }
        ],
        response_format=ATS_Response,
        max_tokens=1024,
        temperature=0.1
        )
    
        return json.loads(response.choices[0].message.content)

