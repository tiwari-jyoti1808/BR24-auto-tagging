'''
Helper to check locally without docker without server
'''

from src import prediction

def predict_locally(article_id, article_data):
    if article_id is None or article_data is None:
        return {'error': 'ID is None'}
    
    results = prediction.compute_tags(article_id, article_data)
    return results

print('Predictions are ::::::::::::::::::::::::', predict_locally(article_id=123, article_data='[TEXT]'))