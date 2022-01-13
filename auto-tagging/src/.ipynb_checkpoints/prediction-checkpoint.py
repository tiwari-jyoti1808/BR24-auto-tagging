'''
Module makes tag predictions
'''

import numpy as np
import requests
import logging
logging.basicConfig(level=logging.DEBUG)

import preprocessing
import postprocessing_in_text
import postprocessing_out_of_text


def compute_tags(article_id, article_data):
    """
    Pre-process text and make in_text and out_of_text predictions.
    
    :param article_id: Article id
    :param article_data: Article text
    
    :return: list of predictions
    """
    
    logging.info('Starting text processing')
    
    # preprocessing of text
    text = preprocessing.text_cleanup(article_data)

    # making in_text tag predictions
    in_text = postprocessing_in_text.in_text_tag_predictions(text)
    
    # making out_of_text tag predictions
    out_of_text = postprocessing_out_of_text.out_of_text_tag_predictions(text)
    
    return list(set(in_text+out_of_text))