'''
Predict in_text tags for a cleaned article text

'''

import logging
logging.basicConfig(level=logging.DEBUG)

import models

spacy_model = models.load_spacy_model()

from stopwords import stopwords

def in_text_tag_predictions(text):
    """
    Make in_text tag predictions following 2 steps:
    1. Entity extraction
    2. Ranking by frequency
    
    :param text: Pre-processed article text
    
    :return: list of in_text predictions
    """
    
    logging.info('Starting text tokenising')
    
    # tokenise pre-processed text
    tokenised_text = spacy_model(text)
    
    logging.info('Starting noun extraction')
    
    # extract noun and proper noun entities using Spacy
    noun_entities = []
    pos_required = ['NOUN', 'PROPN']
    noun_entities = list(set([str(word.orth_) for word in tokenised_text if word.pos_ in pos_required]))
    
    # remove entities which start with a special character or have more than 20 characters as they may be phrases
    noun_entities = [word for word in noun_entities if (len(word) <= 20) & ((word[0].islower()) | (word[0].isupper()))]
    
    logging.info('Starting NER extraction')
    
    # extract ner entities using Spacy
    ner_entities = []
    for ent in tokenised_text.ents:
        if ent.label_ == 'PER' or ent.label_ == 'ORG' or ent.label_ == 'LOC' or ent.label_ == 'MISC':
            ner_entities.append(ent.text)
    
    ner_entities = list(set(ner_entities))

    # remove entities which start with a special character or have more than 20 characters as they may be phrases
    ner_entities = [word for word in ner_entities if (len(word) <= 20) & ((word[0].islower()) | (word[0].isupper()))]

    entities = []
    
    # removing overlap between noun_entities and ner_entities
    entities = ner_entities + list(set(noun_entities) - set(ner_entities))
    
    logging.info('Starting to remove specific stopwords')
    
    # list of words which are nouns, but are not tag worthy
    remove_words = ['Tag', 'Tage', 'Tagen', 'Ihrem', 'BR -Newsletter', 'BR', 'Woche', 'Menschen', 'Wichtigste', 'Personen', 'Jahr', 'Jahren', 'Teil', 'Stadt'] + stopwords
    entities = list(set(entities) - set(remove_words))
    
    #return no predictions if input text is extremely short
    if len(entities)<1:
        return []
    
    logging.info('Starting to rank entities by frequency')
        
    frequency = dict()
    for e in entities:
        frequency[e] = text.count(e.lower())
    
    frequency = dict(sorted(frequency.items(), key=lambda x: len(x[0]), reverse=True))
    
    merged_frequency = dict()
    for e in frequency.keys():
        if not any([e in m for m in merged_frequency.keys()]):
            merged_frequency[e] = frequency[e]
        else:
            key = [k for k in merged_frequency.keys() if e in k][0]
            if merged_frequency[key] < frequency[e]:
                merged_frequency[key] = frequency[e]
    
    merged_frequency = sorted(merged_frequency.items(), key=lambda x: x[1], reverse=True)
    
    predictions = [k[0] for k in merged_frequency[:30]]

    return predictions