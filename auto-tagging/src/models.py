'''
Load models Spacy and USE which are used is text pre-processing and making predictions


'''

import spacy
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import os
import logging
logging.basicConfig(level=logging.DEBUG)


def load_spacy_model():
    '''
    Load spacy model and pass to function call
        
    Returns:
    Spacy model
    '''
    logging.info('Starting Spacy Loading')
    
    nlp = spacy.load('de_core_news_sm')
    return nlp


def load_use_model():
    '''
    Load USE embeddings model and pass to function call
    
    Returns:
    USE embeddings model
    '''
    logging.info('Starting USE Loading')
    
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")
    return embed