# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
#     "requests",
# ]
# ///
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/getquote')
def get_quote():
    try:
        response = requests.get('https://api.freeapi.app/api/v1/public/quotes/quote/random')
        data = response.json()

        if data['success']:
            quote = data['data']
            return {
                'quote': quote['content'],
                'author': quote['author']
            }
        else:
            return {'error': 'Failed to fetch quote'}, 500
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
