import os
import mlflow
import openai
import json
import inspect
import multiprocessing as mp
from  mlflow.metrics.genai import answer_relevance
import pandas as pd


openai.organization = "<Org ID>"
openai.api_key = "<API key>"  
model_name = "gpt-3.5-turbo"


def compute_metrics_for_input(args):
    results = []
    pipeline_code, metrics_code, input = args
    answer_relevance_metric = answer_relevance(model="openai:/gpt-4")
    
    print("Input: ", input)    
    print(pipeline_code)
    print(metrics_code)

    pipeline_locals = {}
    exec(pipeline_code, pipeline_locals)
    pipeline = pipeline_locals['pipeline']
    pipeline_output = pipeline(None, input)

    metrics_locals = {}
    exec(metrics_code, metrics_locals)
    metrics_functions = [v for v in metrics_locals.values() if inspect.isfunction(v)]

    for metrics_function in metrics_functions:
        metrics_output = metrics_function(pipeline_output)
        # print("Pipeline_output type: ", type(pipeline_output), pipeline_output)
        # print("metrics_output type: ", type(metrics_output), metrics_output)
        # print("answer_relevance_metric type: ", type(answer_relevance_metric), answer_relevance_metric)
        print("Pipeline type: ", type(pipeline), pipeline_code)
        print("Input type: ", type(input), input)
        
        eval_data = pd.DataFrame({ 'inputs': [input['topic']] , 'ground_truth': [pipeline_output] , 'predictions': [pipeline_output]})
        print("eval_data type: ", type(eval_data), eval_data)
        with mlflow.start_run() as run:
            results.append(mlflow.evaluate(
            exec(pipeline_code),
            eval_data,
            predictions=metrics_output,
            model_type="question-answering",
            # predictions=metrics_output,
            # extra_metrics=[answer_relevance_metric],
        ))
    return results

def compute_metrics(pipeline_code, metrics_code, inputs):
   inputs_json = json.dumps(inputs)
   inputs_dict = json.loads(inputs_json)

   pool = mp.Pool(mp.cpu_count())
   results = pool.map(compute_metrics_for_input, [(pipeline_code, metrics_code, input) for input in inputs_dict])
   pool.close()

   print("Eval done - now returning the results")
   results = [result for sublist in results for result in sublist]
   return results


# print(compute_metrics(pipeline_code, metrics_code, inputs))