'''
Preprocess article text 
'''

import re

def text_cleanup(text):
    """
    1. Replace HTML tags with punctuations
    2. Remove digits in given text as they would interfere
    3. Remove single characters in given text
    4. Reduce multiple spaces in given text to single space
    
    :param text: Raw article text
    :return: preprocessed article text
    """
    
    # 1. Removes punctuations and '&quote;' in given text
    text = text.replace("&quot;", '\"')
    text = text.replace("’", '')
    text = text.replace("–", '')
    
    # 2. Remove digits in given text
    re_digits = re.compile(r"\d+", re.IGNORECASE)
    text = re.sub(re_digits, " ", str(text))
    
    # 3. Remove single characters in given text
    re_singlechar = re.compile(r"\b[A-Za-z]\b", re.IGNORECASE)
    text = re.sub(re_singlechar, " ", str(text))
    
    # 4. Reduce multiple spaces in given text to single space
    re_wspace = re.compile(r"\s+", re.IGNORECASE)
    text = re.sub(re_wspace, " ", str(text))
    
    return text