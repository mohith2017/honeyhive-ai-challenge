#An attempt to manually classify all pipelines into custom llm evaluator type using Decision tree
import numpy as np
import inspect
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import LabelBinarizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

def classify(pipeline):
    prompts = [ """prompt = "You are a helpful assistant. Write an essay on the topic of {input['topic']}.""", """prompt = f"You are a helpful assistant. Write a story about a character named {input['character']} in the setting of {input['setting']}.""", 
                         """prompt = "You are a helpful assistant. Write a summary of the following text: {input['text']}""", 
                         """prompt = "You are a helpful assistant. Generate a list of questions based on the following text: {input['text']}""",
                         """prompt = "You are a helpful assistant. Write a poem about the theme of {input['theme']}.""",
                         """prompt = "You are a helpful assistant. Write a recipe using the following ingredients: {input['ingredients']}""",
                         """prompt = "You are a helpful assistant. Generate a list of possible solutions to the problem: {input['problem']}""",
                         """prompt = "You are a helpful assistant. Write a short story about the plot: {input['plot']}""",
                         """prompt = "You are a helpful assistant. Write a report based on the following data: {input['data']}"""]
    
    # Create a TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the prompts into a matrix of TF-IDF features
    tfidf_matrix = vectorizer.fit_transform(prompts)
    features = tfidf_matrix.toarray()

    labels = np.array(["text-classification", "token-classification", "question-answering", "image-classification", "text-generation", "text2text-generation", "summarization", "translation", "automatic-speech-recognition" ]) # replace with your labels

    # Create a LabelBinarizer
    lb = LabelBinarizer()

    # Fit and transform the labels into a binary matrix
    y = lb.fit_transform(labels)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Create a Decision Tree Classifier
    clf = DecisionTreeClassifier()

    # Train the classifier
    clf.fit(X_train, y_train)

    # Use the trained classifier to make predictions on the testing data
    predictions = clf.predict(pipeline)

    return predictions



def func_to_str(func):
   return inspect.getsource(func)


functions = [
   """def pipeline(config, input):
        prompt = f"You are a helpful assistant. Write an email on the topic of {input['topic']}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']"""
   # Add other functions here
]

function_strs = [func_to_str(func) for func in functions]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(function_strs)
input = tfidf_matrix.toarray()



print(classify(input))
