import time
import json 
from flask import Flask, render_template
from backend.report import generate_report
from backend.compute import compute_metrics
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField, SubmitField
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, redirect, url_for
from flask import session, request

app = Flask(__name__)


# Set the secret key
app.config['SECRET_KEY'] = b'\x99=\x19(\xfe\xbd\xe0]\xfe7\xe8\xc3\xe6\xd4\xef\xeer\x85\xaf1\xbf9\xce:'
csrf = CSRFProtect(app)

class MetricsForm(FlaskForm):
   pipeline_code = TextAreaField('Pipeline Code')
   metrics_code = TextAreaField('Metrics Code')
   input_file = FileField('Input File (JSON)')
   submit = SubmitField('Submit')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# class TaskResult(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    task_id = db.Column(db.String(36), unique=True, nullable=False)
#    result = db.Column(db.PickleType, nullable=True)

# with app.app_context():
#    db.create_all()
   
##For testing
# pipeline_code = """import openai
# def pipeline(config, input):
#         prompt = f"You are a helpful assistant. Write an email on the topic of {input['topic']}"
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message['content']"""



# inputs = """[
#         {
#             "topic": "enterprise SaaS pitch",
#             "input_metadata": {
#                 "importance": 0.9
#             }
#         },
#         {
#             "topic": "marketing campaign",
#             "input_metadata": {
#                 "importance": 0.5
#             }
#         }
#         ]"""

# metrics_code = """import openai
# def email_quality(output):
#         prompt = f"You are a helpful assistant. Give the following email a 1-5 score: {output}"
#         response = openai.ChatCompletion.create(
#             model="gpt-4", 
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message['content']"""

@app.route('/', methods=['GET', 'POST'])
def index():
   form = MetricsForm()
   if form.validate_on_submit():
      session['pipeline_code'] = "import openai\n" + form.pipeline_code.data
      session['metrics_code'] = "import openai\n" + form.metrics_code.data
      
      input_file = form.input_file.data
      print("Request:", input_file)
      if input_file:
            file_contents = input_file.read().decode('utf-8')
            try:
                input_json = json.loads(file_contents)
                session['input_file'] = input_json
                print("Input json", input_json)
            except json.JSONDecodeError as e:
                print("JSON decoding error:", e)                

      return redirect(url_for('report'))


   return render_template('index.html', form=form)


@app.route('/report', methods=['GET'])
def report():
   # pipeline_code = session.get('pipeline_code')
   # metrics_code = session.get('metrics_code')
   # inputs =  session.get('inputs')
   output_metadata = compute_metrics(session['pipeline_code'], session['metrics_code'], session['input_file'])
   report = generate_report(output_metadata)
   # output = output_metadata.get()
   # print(report)
   # while not output_metadata.ready():
   #    time.sleep(1)

   # task_result = TaskResult.query.filter_by(task_id=output_metadata.id).first()
   # if task_result and task_result.result:
   #     report = generate_report(task_result.result)
   # else:
   #     # The task has not completed yet
   #     report = None

   return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)


