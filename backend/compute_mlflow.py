import inspect
import json
import mlflow
import multiprocessing as mp
import pandas as pd

#An attempt to compute metrics using mlflow by Databricks

def compute_metrics(pipeline_code, metrics_code, input):
    inputs_json = json.dumps(input)
    inputs_dict = json.loads(inputs_json)

    
    pool = mp.Pool(mp.cpu_count())
    pool.map(evaluate, [(pipeline_code, metrics_code, input) for input in inputs_dict])


def evaluate(pipeline_code, metrics_code, input):

    pipeline_locals = {}
    exec(pipeline_code, pipeline_locals)
    pipeline = pipeline_locals['pipeline']

    metrics_locals = {}
    exec(metrics_code, metrics_locals)
    metrics_functions = [v for v in metrics_locals.values() if inspect.isfunction(v)]


eval_data = pd.DataFrame(
    {
        "inputs": [
            "What is MLflow?",
            "What is Spark?",
        ],
        "ground_truth": [
            "MLflow is an open-source platform for managing the end-to-end machine learning (ML) lifecycle. It was developed by Databricks, a company that specializes in big data and machine learning solutions. MLflow is designed to address the challenges that data scientists and machine learning engineers face when developing, training, and deploying machine learning models.",
            "Apache Spark is an open-source, distributed computing system designed for big data processing and analytics. It was developed in response to limitations of the Hadoop MapReduce computing model, offering improvements in speed and ease of use. Spark provides libraries for various tasks such as data ingestion, processing, and analysis through its components like Spark SQL for structured data, Spark Streaming for real-time data processing, and MLlib for machine learning tasks",
        ],
    }
)


def openai_qa(inputs):
    answers = []
    system_prompt = "Please answer the following question in formal language."
    for index, row in inputs.iterrows():
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "{row}"},
            ],
        )
        answers.append(completion.choices[0].message.content)

    return answers


with mlflow.start_run() as run:
    results = mlflow.evaluate(
        openai_qa,
        eval_data,
        model_type="question-answering",
    )
    
