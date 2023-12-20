from celery import Celery
import os
import openai
import json
import inspect

openai.organization = "org-PDgZdabgwEQG4CKvJHhH4ALa"
openai.api_key = "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"  
model_name = "gpt-3.5-turbo"

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def compute_metrics(pipeline_code, metrics_code, inputs):
    results = []
    
    inputs_json = json.dumps(inputs)
    inputs_dict = json.loads(inputs_json)
    print("Input: ", type(inputs_dict))    

    print(pipeline_code)
    print(metrics_code)

    for input in inputs_dict:
        # Create a local scope for the pipeline code
        pipeline_locals = {}
        exec(pipeline_code, pipeline_locals)
        pipeline = pipeline_locals['pipeline']
        pipeline_output = pipeline(None, input)

        # Execute the metrics code
        metrics_locals = {}
        exec(metrics_code, metrics_locals)
        # Get the metrics functions from the local scope
        metrics_functions = [v for v in metrics_locals.values() if inspect.isfunction(v)]

        for metrics_function in metrics_functions:
            metrics_output = metrics_function(pipeline_output)
            # Save the results
            results.append({
                'input': input,
                'pipeline_output': pipeline_output,
                'metrics_output': metrics_output
            })
    return results


# print(compute_metrics(pipeline_code, metrics_code, inputs))