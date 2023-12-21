import inspect
from datasets import load_dataset
from sklearn.pipeline import Pipeline
from evaluate import evaluator

class ScikitEvalPipeline:
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.task = "text-classification"

    def __call__(self, input_texts, **kwargs):
        return [{"label": p} for p in self.pipeline.predict(input_texts)]


def compute_metrics(pipeline, metrics, data):
    result = []
    pipe = ScikitEvalPipeline(pipeline)
    task_evaluator = evaluator(pipe)

    metrics_locals = {}
    exec(metrics, metrics_locals)
    metrics_functions = [v for v in metrics_locals.values() if inspect.isfunction(v)]

    for metrics_function in metrics_functions:
        result.append(
        eval_results = task_evaluator.compute(
        model_or_pipeline="gpt-3.5",
        data=data,
        label_mapping={"NEGATIVE": 0, "POSITIVE": 1},
        metric=metrics_function)
        )

    return result


print(compute_metrics("""def pipeline(config, input):
        prompt = f"You are a helpful assistant. Write an email on the topic of {input['topic']}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']""", """[
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
        ]""", """def email_quality(output):
        prompt = f"You are a helpful assistant. Give the following email a 1-5 score: {output}"
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']"""))



