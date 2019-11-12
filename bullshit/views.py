from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
import spacy

# Create your views here.
def home(request):
    output = list()
    nlp = spacy.load("fr_core_news_sm")

    file = open("aggregated_by_topic/politique/politique_article1.txt", "r")
    doc = nlp(file.read())

    for num, sentence in enumerate(doc.sents):
        output.append(sentence.lemma_)
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'bullshit/index.html', {'output': output})
