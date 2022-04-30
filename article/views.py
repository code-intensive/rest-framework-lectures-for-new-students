from http import HTTPStatus
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def articles_list(request:HttpRequest):
    if request.method == 'GET':
        articles = Article.objects.all()
        serialized_articles = ArticleSerializer(articles, many=True)
        return Response(serialized_articles.data, status=HTTPStatus.OK)


@api_view(['POST'])
@csrf_exempt
def create_article(request:HttpRequest):
    if request.method == 'POST':
        parsed_request = JSONParser().parse(request)
        serialized_article = ArticleSerializer(data=parsed_request)
        if serialized_article.is_valid():
            serialized_article.save()
            return Response(serialized_article.data, status=HTTPStatus.CREATED)
        return Response(serialized_article.errors, status=HTTPStatus.EXPECTATION_FAILED)


@api_view(['GET'])
@csrf_exempt
def article_detail(request:HttpRequest, pk:int):
    if request.method == 'GET':
        article = Article.objects.filter(pk=pk)
        if article.exists():
            article = article.first()
            serialized_article = ArticleSerializer(article)
            return Response(serialized_article.data, status=HTTPStatus.OK)
        return Response({'error_message': 'Article does not exist'}, status=HTTPStatus.NOT_FOUND)
