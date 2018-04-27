from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation
import string

def home(request):
    return render(request,'home.html',{'hithere':'This is me'})
def count(request):
    fullTextHere=request.GET['fullTextHere']
    print(fullTextHere)
    fullTextHere=fullTextHere.lower()
    fullTextHere=fullTextHere.replace(",", "")
    fullTextHere=fullTextHere.replace("?", "")
    wordlist=fullTextHere.split()
   
    worddict={}
    for word in wordlist:
        
        if word in worddict:
            
            worddict[word]+=1
        else:
            worddict[word]=1
    return render(request,'count.html',{'fullTextHere':fullTextHere,'count':len(wordlist), 'worddict':worddict.items })
def about(request):
    return render(request,'about.html')