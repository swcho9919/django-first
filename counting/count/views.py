from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def result(request):
#     print(request)
#     text = request.GET['fulltext']
#     textcount = len(text)
#     splitted_text = text.split()
#     text2 = "".join(splitted_text)
#     text2count = len(text2) 
#     return render(request, 'result.html', {
#         'text': text,
#         'textcount': textcount,
#         'text2count': text2count,
#     })

def wordcount_result(request):
    print(request)
    frequency = {}
    text = request.GET['fulltext']
    splitted_text = text.split()
    wordcount = len(splitted_text) 

    for word in splitted_text:
        count = frequency.get(word,0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        print (words, frequency[words])

    return render(request, 'wordcount_result.html', {
        'text': text,
        'wordcount': wordcount,
        'frequency' : frequency,
    })
