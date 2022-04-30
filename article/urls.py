from django.urls import path
from article.views import articles_list, create_article, article_detail


app_name = 'article'
urlpatterns = [
    path('articles/', articles_list, name='articles'),
    path('create/', create_article, name='create'),
    path('detail/<int:pk>/', article_detail, name='detail'),
]
