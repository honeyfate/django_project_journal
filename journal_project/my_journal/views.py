from django.shortcuts import render

def journal_list(request):
    return render(request, 'my_journal/journal_list.html')