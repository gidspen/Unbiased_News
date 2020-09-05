'''
This script is V1 for removing bias parts of spech from a sentence.
To understand the parts of speech abbreviation, reference: https://sites.google.com/site/partofspeechhelp/home

'''

from nltk import word_tokenize
from nltk import pos_tag

def debiase(sentence):
    
    s1 = sentence

    tokens = word_tokenize(s1)

    tagged = pos_tag(tokens)
    unbiased_dict = {}
    unbiased_sent = []

    for grouping in tagged:
        key = grouping[0]
        value = grouping[1]
        unbiased_dict[key] = value

    for key, value in unbiased_dict.items():
        if value in ('JJ', 'JJS', 'RB'):
            continue
        elif value in (".", "?", "!"):
            unbiased_sent.append(key)
        else:
            unbiased_sent.append(" " + key)

    return ''.join(unbiased_sent)



print(debiase('trump said another stupid thing today. he made a dumb comment about his beautiful hair.'))
