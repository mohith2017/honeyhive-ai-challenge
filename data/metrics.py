import os
import openai

openai.organization = "YOUR_ORG_ID"
openai.api_key = "YOUR API KEY"
model_name="gpt-3.5-turbo"

def email_quality(output):
   prompt = f"You are a helpful assistant. Evaluate the quality of the following email: {output}"
   response = openai.ChatCompletion.create(
       model="gpt-4",
       messages=[{'role': 'user', 'content': prompt}]
   )
   return response.choices[0].message['content']