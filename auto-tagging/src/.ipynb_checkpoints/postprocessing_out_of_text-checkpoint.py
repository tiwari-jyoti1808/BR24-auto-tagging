'''
Predict out_of_text tags for a cleaned article text

'''

import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG)

import models

use_model = models.load_use_model()

from low_level_categories import low_level_categories

def out_of_text_tag_predictions(text):
    """
    Make out_of_text tag predictions following 2 steps:
    1. Predict low-level categories for the article
    2. Predict most similar tags from the low-level categories
    
    :param text: Pre-processed article text
    
    :return: list of out_of_text predictions
    """
    
    logging.info('Starting low-level category prediction')
    
    categories_embedding = np.zeros(shape=(30,512)) # initialize with zeroes as there are 30 low-level categories

    # Calculating tag cluster embeddings
    for idx, c in enumerate(list(low_level_categories.keys())): 
        category_embeddings = use_model(c) # embedding of the low-level category name
        value_embeddings = np.mean(use_model(low_level_categories[c]), axis=0) # mean of all tag embeddings in the low-level category
        cluster_embeddings = (np.array(category_embeddings) + np.array(value_embeddings)) / 2 # mean of embeddings of the low-level category name and the tags in the low-level category. This forms the tag cluster embeddings
        categories_embedding[idx] = cluster_embeddings
        
    # Predicting low-level category for the article
    article_embedding = use_model(text[:20000]).numpy()
    distances = np.dot(article_embedding, np.transpose(categories_embedding))[0]
    category_indices = distances.argsort()[-3:][::-1]
    categories = [list(low_level_categories)[c] for c in category_indices]
    
    # Predicting tags from the low-level categories for the article
    tag_list = low_level_categories[categories[0]]+low_level_categories[categories[1]]+low_level_categories[categories[2]]
    tag_embedding = use_model(tag_list).numpy()
    
    distances = np.dot(tag_embedding, article_embedding.reshape(-1,1))
    zipped = zip(distances, tag_list)
    sorted_zipped = sorted(zipped, key = lambda t: t[0])
    tags = list(list(zip(*sorted_zipped[-10:]))[1:][0])
    tags.reverse()
    
    return tags