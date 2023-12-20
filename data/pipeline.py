import os
import openai

openai.organization = "YOUR_ORG_ID"
openai.api_key = "YOUR API KEY"
model_name="gpt-3.5-turbo"


# Pipeline 1: Generate a summary of a given text.

def pipeline1(config, input):
  prompt = f"You are a helpful assistant. Write a summary of the following text: {input}"
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}]
  )
  return response.choices[0].message['content']



# Pipeline 2: Translate a given text to a different language.

def pipeline2(config, input):
  prompt = f"You are a helpful assistant. Translate the following text to French: {input}"
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}]
  )
  return response.choices[0].message['content']


# Pipeline 3: Write a story based on a given character and setting.

def pipeline3(config, input):
  prompt = f"You are a helpful assistant. Write a short story about a character named {input['character']} in the setting of {input['setting']}."
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}]
  )
  return response.choices[0].message['content']



# Pipeline 4: Generate a list of questions based on a given text.

def pipeline4(config, input):
  prompt = f"You are a helpful assistant. Generate a list of questions based on the following text: {input}"
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}]
  )
  return response.choices[0].message['content']

# Pipeline 5: Write an essay on a given topic.

def pipeline5(config, input):
  prompt = f"You are a helpful assistant. Write an essay on the topic of {input['topic']}."
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}]
  )
  return response.choices[0].message['content']


###Sample direct data:

def pipeline(config, input):
        prompt = f"You are a helpful assistant. Write an email on the topic of {input['topic']}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']



[
        {
            "topic": "enterprise SaaS pitch",
            "input_metadata": {
                "importance": 0.9
            }
        },
        {
            "topic": "marketing campaign",
            "input_metadata": {
                "importance": 0.5
            }
        }
        ]

def email_quality(output):
        prompt = f"You are a helpful assistant. Give the following email a 1-5 score: {output}"
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']


# Pipeline 1:
# prompt = f"You are a helpful assistant. Write an essay on the topic of {input['topic']}."
# Pipeline 2:
# prompt = f"You are a helpful assistant. Write a story about a character named {input['character']} in the setting of {input['setting']}."
# Pipeline 3:
# prompt = f"You are a helpful assistant. Write a summary of the following text: {input['text']}"
# Pipeline 4:
# prompt = f"You are a helpful assistant. Generate a list of questions based on the following text: {input['text']}"
# Pipeline 5:
# prompt = f"You are a helpful assistant. Write a poem about the theme of {input['theme']}."
# Pipeline 6:
# prompt = f"You are a helpful assistant. Write a recipe using the following ingredients: {input['ingredients']}"
# Pipeline 7:
# prompt = f"You are a helpful assistant. Generate a list of possible solutions to the problem: {input['problem']}"
# Pipeline 8:
# prompt = f"You are a helpful assistant. Write a short story about the plot: {input['plot']}"
# Pipeline 9:
# prompt = f"You are a helpful assistant. Write a report based on the following data: {input['data']}"
# Pipeline 10:
# prompt = f"You are a helpful assistant. Write a business plan for the business idea: {input['business_idea']}"
# Pipeline 11:
# prompt = f"You are a helpful assistant. Generate a list of possible strategies for the market: {input['market']}"
# Pipeline 12:
# prompt = f"You are a helpful assistant. Write a song about the theme of {input['theme']}."
# Pipeline 13:
# prompt = f"You are a helpful assistant. Write a book review for the book: {input['book']}"
# Pipeline 14:
# prompt = f"You are a helpful assistant. Generate a list of possible features for the product: {input['product']}"
# Pipeline 15:
# prompt = f"You are a helpful assistant. Write a resume based on the following experiences: {input['experiences']}"
# Pipeline 16:
# prompt = f"You are a helpful assistant. Generate a list of possible locations for the event: {input['event']}"
# Pipeline 17:
# prompt = f"You are a helpful assistant. Write a script for a play about the plot: {input['plot']}"
# Pipeline 18:
# prompt = f"You are a helpful assistant. Translate the following text to {input['language']}: {input['text']}"
# Pipeline 19:
# prompt = f"You are a helpful assistant. Write a book review for the book: {input['book']}"
# Pipeline 20:
# prompt = f"You are a helpful assistant. Generate a list of possible promotions for the product: {input['product']}"
# Pipeline 21:
# prompt = f"You are a helpful assistant. Write an essay on the topic of {input['topic']}."
# Pipeline 22:
# prompt = f"You are a helpful assistant. Translate the following text to {input['language']}: {input['text']}"
# Pipeline 23:
# prompt = f"You are a helpful assistant. Write a business plan for the business idea: {input['business_idea']}"
# Pipeline 24:
# prompt = f"You are a helpful assistant. Generate a list of possible strategies for the market: {input['market']}"
# Pipeline 25:
# prompt = f"You are a helpful assistant. Write a song about the theme of {input['theme']}."
# Pipeline 26:
# prompt = f"You are a helpful assistant. Translate the following text to {input['language']}: {input['text']}"
# Pipeline 27:
# prompt = f"You are a helpful assistant. Write a resume based on the following experiences: {input['experiences']}"
# Pipeline 28:
# prompt = f"You are a helpful assistant. Generate a list of possible promotions for the product: {input['product']}"
# Pipeline 29:
# prompt = f"You are a helpful assistant. Write a novel about the plot: {input['plot']}"
# Pipeline 30:
# prompt = f"You are a helpful assistant. Write a novel about the plot: {input['plot']}"
