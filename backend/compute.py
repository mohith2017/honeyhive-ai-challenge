from celery import Celery
import os
import openai
import json
import inspect
import multiprocessing as mp


openai.organization = "<YOUR ORG ID>"
openai.api_key = "<YOUR OPEN AI API KEY>"  
model_name = "gpt-3.5-turbo"

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def compute_metrics_for_input(args):
    results = []
    pipeline_code, metrics_code, input = args
    
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
        results.append({
            'input': input,
            'pipeline_output': pipeline_output,
            'metrics_output': metrics_output
        })
    return results

def compute_metrics(pipeline_code, metrics_code, inputs):
   inputs_json = json.dumps(inputs)
   inputs_dict = json.loads(inputs_json)

   pool = mp.Pool(mp.cpu_count())
   results = pool.map(compute_metrics_for_input, [(pipeline_code, metrics_code, input) for input in inputs_dict])
   pool.close()

   results = [result for sublist in results for result in sublist]
   return results


# print(compute_metrics(pipeline_code, metrics_code, inputs))