#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup1 = len(sentence)
        tup2 = "None"
    else:
        tup1 = len(sentence)
        tup2 = sentence[0]
    res = (tup1, tup2)
    return res
