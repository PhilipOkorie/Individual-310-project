import stanza
import truecase
from SynonymNLTK import *

name = "John"
def processpos(msg):

    resp = ""
    nlp = stanza.Pipeline(lang = "en", processors = "tokenize,pos") # Build the pipeline, specify part-of-speech processor's batch size
    msg = truecase.get_true_case(msg)
    msg1 = nlp(msg)
    pos_VerbAux = [word.text for sent in msg1.sentences for word in sent.words if word.upos in ["VERB", "AUX", "ADJ"]]


    if len(pos_VerbAux) > 0 :
        #these list comprehension is used to extract the tense or verb form from the features(.feats) attribute from every item where "Tense=" or "VerbForm=" is in the list
        tense = [word[word.find("Tense")+6:word.find("Tense")+10] if "Tense=" in word  else None for word in [item[1] for item in pos_VerbAux]]
        verbForm = [word[word.find("VerbForm")+9: word.find("VerbForm")+12]  if "VerbForm=" in word else None for word in [item[1] for item in pos_VerbAux]]


        #this list comprehension is just used to remove any None value in our lists
        tense = [i for i in tense if i]
        verbForm = [i for i in verbForm if i]
        #for word in pos_VerbAux:
         #   if "ADJ" in word.upos:
          #      resp = "Thanks for giving a description! \n"
        #if("Past" in tense):
         #   resp = resp + " It's in the past now!"
        #elif "Fin" in verbForm:
         #   resp = resp + " I see. That will work out!"
        resp = detectsyn(pos_VerbAux)

    else:
        resp = ""

    return resp

