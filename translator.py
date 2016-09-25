"""Contain all the tools to translate
"""

def lower_case(sentence=None):
    if sentence is None:
        raise Exception("None sentence")

    return sentence.lower()

def split(sentence=None):
    """split a sentence in words lower case
    must detect numbers and ponctiation
    """

    lower_case_sentence = lower_case(sentence=sentence)

    return lower_case_sentence.split(' ')

def process_translation(msg=None):
    if msg is not None:
        split_sentence = split(sentence=msg)
        return ' '.join(split_sentence)
    else:
        return "Empty message"
