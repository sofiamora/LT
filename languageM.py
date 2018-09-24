
import regex as re
import sys
import math

def normalize (text) :
    text = re.sub(r'(\.{2,})' , '' , text)
    text = re.sub('[^(\p{L}+\.)]', ' ', text) # cambia todos los que no sean letras y punto s por espacios
    #text = re.sub(r'((\p{L}+) *)*(\.)', r' \3 </s>\n', text)
    text = re.sub('(\.)', '</s> \n <s>', text)
    #text = text.lower()
    text = '<s>'+ text;
    text = text[:-7]
    return text

def tokenize(text):
    words= re.findall('\p{L}+',text)
    return words

def countUnigrams (words):
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency

def probabilityUni(length, words):
    probability={}
    for word in words:
        probability[word] = words[word]/length
    return probability

if __name__ == '__main__':
    text = sys.stdin.read().lower()
    #print (normalize(text))
    words = tokenize(text)
    cuenta = countUnigrams(words)
    proba = probabilityUni(len(cuenta), cuenta)
    print('Probabilidad Unigramas\nwi     C(wi)     #words     P(wi)')
    for uni in proba:
        print(uni +'   '+ str(cuenta[uni]) +'          ' +str(len(words))+'         '+str(proba[uni]))

