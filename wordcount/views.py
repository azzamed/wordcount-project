from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #return render(request, 'home.html', {'hithere':'azza'})
    return render(request, 'home.html')

def count(request):
    #return render(request, 'home.html', {'hithere':'azza'})
    fulltext = request.GET['fulltext']
    wordlist=fulltext.split()

    wor_dic={}
    for word in wordlist:
        if word in wor_dic:
            wor_dic[word] += 1
        else:
            wor_dic[word] = 1

    sortedwords=sorted(wor_dic.items(), key=operator.itemgetter(1), reverse=True)
    print(fulltext)
    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
# def eggs(request):
    #return HttpResponse('Eggs are great!')
    #return HttpResponse('<h1>Eggs are great!</h1>')
    #return HttpResponse('')
