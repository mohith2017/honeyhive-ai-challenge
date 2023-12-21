# About
Honey Hive AI LLM Eval application. Built on Flask, python and OpenAI's GPT-3.5 LLM API with custom evaluation and metrics for LLM Eval.

# Structure

```
.
├── backend
│   ├── classify.py
│   ├── compute.py
│   ├── compute_mlflow.py
│   ├── compute_ray.py
│   ├── report.py
│   └── secret_key.py
├── data
│   ├── input.py
│   ├── inputs.json
│   ├── metrics.py
│   └── pipeline.py
├── routes.py
├── static
│   └── css
│       ├── index.css
│       └── report.css
└── templates
    ├── index.html
    └── report.html
```



# App screenshots

![App screenshot](https://i.ibb.co/GTVXHV2/Report-challenge.png) <br>
![App screenshot](https://i.ibb.co/rw57YMc/Frontend-UI.png)



# Additional files
Within the repository, there are few files that are non-relevant to the challenge, 
but are other experimental ways of implementing the backend parallel computation of the LLM pipelines using:

- MLflow by Databricks
- HuggingFace evaluator


# Running the application
To run the application locally, navigate to the main directory:

`$ python3 routes.py`

And navigating to the localhost link in the terminal on any browser of your choice.


# Tech Stack
- Frontend: Flask, python based HTML, CSS and app routing. 
- Backend:  Python based parallel computation
- LLM: OpenAI's GPT-3.5 LLM



# Workflow

![App workflow](https://example.com/image.jpg)

# Sample Data

## Function Data
```
def pipeline(config, input): \n
        prompt =
        f"You are a helpful assistant. Write an email on the topic of {input['topic']}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
```

## Input Data

```
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
```

## Metrics Data

```
def email_quality(output):
        prompt = f"You are a helpful assistant. Give the following email a 1-5 score: {output}"
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
```
