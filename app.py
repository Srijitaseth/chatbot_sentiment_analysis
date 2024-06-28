from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__, static_url_path='/static')
sentiment_analyzer = pipeline('sentiment-analysis')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    sentiment = sentiment_analyzer(user_input)[0]
    return render_template('response.html', user_input=user_input, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
