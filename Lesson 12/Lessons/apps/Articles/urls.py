from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create, name = 'create'),
    path('<int:a_id>/', views.article, name = 'article'),
    path('<int:a_id>/edit', views.edit, name = 'edit'),
    path('<int:a_id>/delete', views.delete, name = 'delete'),
    path('<int:a_id>/comment', views.comment, name = 'comment'),
]