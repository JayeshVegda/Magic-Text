# new file hehhehe
from django.http import HttpResponse
from django.shortcuts import render
import  re
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text')
    removefunc = request.POST.get('removefunc')
    CapitalizedFirst = request.POST.get('CapitalizedFirst')
    newline = request.POST.get('newline')
    RemoveSpace = request.POST.get('RemoveSpace')
    CharCount = request.POST.get('CharCount')

    if removefunc == "on":
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        parm = {'type': 'Remove Punctuation', 'data': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', parm)
    if CapitalizedFirst == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parm = {'type': 'Capitalized First', 'data': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', parm)
    if RemoveSpace == "on":
        pat = '\s+'
        s = re.sub(pat, "", djtext)
        parm = {'type': 'White Space Remover', 'data': s}
        djtext = s
        #return render(request, 'analyze.html', parm)

    if newline == "on":
        pat = '/n'
        s = re.sub(pat, "", djtext)
        parm = {'type': 'New Line Remover', 'data': s}
        djtext = s
        #return render(request, 'analyze.html', parm)

    if CharCount == "on":
        len1 = len(djtext)
        parm = {'type': 'Charecter Counter ', 'data': len1}
        djtext = len1
        # return render(request, 'analyze.html', parm)

    if(removefunc != "on", CharCount != "on",  newline != "on", RemoveSpace != "on", CapitalizedFirst != "on"):
        parm = {'type': 'NOT SELECTED ', 'data': djtext}
        return render(request, 'analyze.html', parm)

    return render(request, 'analyze.html', parm)
