import numpy as np
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    """Predict answer to the user question."""
    questions = [str(x) for x in request.form.values()]
    question = str(questions[0])
    # answer = predict(question)
    reader = pipeline("question-answering")
  # question = "What does the customer want?"
    df = pd.read_excel('pdf_extract_test.xlsx')
    text_list = df.content.tolist()
    text = " ".join(text_list)
    outputs = reader(question=question, context=text)
    op_df = pd.DataFrame.from_records([outputs])
    answer = str(op_df['answer'].iloc[0])
    return render_template('index.html', prediction_text='Predicted answer for "'+question+'" :  {}'.format(answer))
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8282, debug=True)