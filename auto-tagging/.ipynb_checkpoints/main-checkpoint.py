'''
Helper to check locally without docker with server
'''

import random
from flask import Flask, request, jsonify
from src import prediction
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/predict', methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        json_data = request.json
        article_id = json_data['id']
        article_data = json_data['data']
        # articles_id = request.form.get('id')
        if article_id is None:
            jsonify({'error': 'ID is None'})
        if article_data is None:
            jsonify({'error': 'Data is None'})
        
        results = prediction.compute_tags(article_id, article_data)
        
        # Model computation
        return jsonify({
            'id': article_id,
            'data': results})

    return "OK" # Health Check 


if __name__== "__main__":
    app.run(debug=True)

