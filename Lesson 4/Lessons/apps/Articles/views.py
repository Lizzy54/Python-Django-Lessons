from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Article

def index(request):
    articles_list = Article.objects.order_by('-date')
    return render(request, 'articles/list.html', {'articles_list': articles_list})

def article(request, a_id):
    try:
        a = Article.objects.get( id = a_id )
    except:
        raise Http404("Страница не найдена")
    return render(request, 'articles/article.html', {'article': a})
