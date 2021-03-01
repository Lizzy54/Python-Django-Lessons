from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import datetime

from .models import Article, Comment

def index(request):
    articles_list = Article.objects.order_by('-date')
    return render(request, 'articles/list.html', {'user': request.user, 'articles_list': articles_list})
    
    # return HttpResponse(request.user.has_perm('Articles.can_change_article'))

def article(request, a_id):
    try:
        a = Article.objects.get( id = a_id )
    except:
        raise Http404("Страница не найдена")
    comments_list = Comment.objects.filter( article_id = a_id )
    return render(request, 'articles/article.html', {'user': request.user, 'article': a, 'comments': comments_list})

def create(request):
    if request.method == "GET":
        return render(request, 'articles/create.html', {'user': request.user, 'url': '/articles/create', 'title': 'Создание статьи'})
    elif request.method == "POST":
        article = Article()
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.date = datetime.datetime.now()
        article.save()
        return HttpResponseRedirect('/articles')

def edit(request, a_id):
    if request.method == "GET":
        url = '/articles/' + str(a_id) + '/edit'
        a = Article.objects.get( id = a_id )
        return render(request, 'articles/create.html', {'user': request.user, 'url': url, 'article': a, 'title': a.title})
    elif request.method == "POST":
        a = Article.objects.get( id = a_id )
        a.title = request.POST.get("title")
        a.text = request.POST.get("text")
        a.date = datetime.datetime.now()
        a.save()
        return HttpResponseRedirect('/articles')
        
def delete(request, a_id):
    if request.user.has_perm('Articles.delete_article'):
        Article.objects.filter( id = a_id ).delete()
        comments_list = Comment.objects.filter( article_id = a_id ).delete()
    return HttpResponseRedirect('/articles')

def comment(request, a_id):
    if request.user.is_authenticated:
        comment = Comment()
        comment.name = request.user
        comment.text = request.POST.get("text")
        comment.date = datetime.datetime.now()
        comment.article_id = a_id
        comment.save()
    return HttpResponseRedirect('/articles/' + str(a_id))