import stanza
import truecase
from Chatbot import *

#stanza.download('en')

def processinput(msg):
    
    resp = ""
    nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") # Build the pipeline, specify part-of-speech processor's batch size
    msg = truecase.get_true_case(msg)
    msg1 = nlp(msg)
    ner_workOfArt = [token.text for sentences in msg1.sentences for token in sentences.tokens if "WORK_OF_ART" in token.ner]

    if len(ner_workOfArt)>0:
        for finalwords in ner_workOfArt:
            resp = resp + "I have heard about " + finalwords + ". It is a great work of art! \n" 
            return resp
            
        
        #return resp
        
    resp = ""
    return resp
    