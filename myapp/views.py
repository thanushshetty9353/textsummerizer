from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,'index.html')

def analyzer(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    analyzed = text 
    if removepunc == "on":
        punctuations = ''':;{}()-[]'"\,/<>@!#$%^&*'''
        analyzed = ""  
        for char in text:
            if char not in punctuations:
                analyzed += char

    if capitalize == "on":
        updated_text = "" 
        for char in analyzed:
            updated_text += char.upper()
        analyzed = updated_text 
    
    if newlineremover == "on":
        nanalyzed = ""  
        for char in analyzed:
            if char!="\n" and char!="\r":
                nanalyzed += char
        analyzed = nanalyzed
        
    if extraspaceremover == "on":
        result = analyzed[0]  
        for i in range(1, len(analyzed)):  
            if not (analyzed[i] == " " and analyzed[i - 1] == " "):  
                result += analyzed[i]  
        analyzed = result  

    if removepunc == "on" or capitalize == "on" or newlineremover =="on" or extraspaceremover == "on" :
        params = {"purpose": "Text Processing", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select at least one option.")
