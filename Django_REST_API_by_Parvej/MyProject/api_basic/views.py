import sys

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .spFolder.storedProcedures import Insert_Article_Comment


# Create your views here.

# CREATING METHODS FOR GENERICS API VIEWS AND MIXINS
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    # For Session or Basic authentication
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

    # For Token Authentication use below
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# CREATING METHODS USING VIEWSETS - ViewSet
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()

        print(articles)

        # convert the queryset article using serializer
        serializer = ArticleSerializer(articles, many=True)

        print(serializer.data)
        # return Response(request.data)

    def create(self, request):
        print(request.data)
        serializer = ArticleSerializer(data=request.data)

        print(serializer)
        # sys.exit('server error')

        if serializer.is_valid():
            serializer.save()
            savedId = serializer.data['id']
            comment = "Added A New article with Article ID " + str(savedId)
            Insert_Article_Comment(savedId, comment)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # For getting list by id
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CREATING METHODS USING VIEWSETS - GenericViewSet
class ArticleGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin
    , mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# CREATING METHODS USING VIEWSETS - ModelViewSet
class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    # For getting list by id
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ALL METHODS CALLED USING CLASS BASED VIEWS
class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()

        # convert the queryset article using serializer
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def article_list(request):
    if request.method == 'GET':
        # Fetch all Articles from the database
        articles = Article.objects.all()

        # convert the queryset article using serializer
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        article_data = JSONParser().parse(request)

        serializer = ArticleSerializer(data=article_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
# For getting a particular article using its id
def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        # convert the queryset article using serializer
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        article_data = JSONParser().parse(request)

        serializer = ArticleSerializer(article, data=article_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)


# ALL METHODS CALLED USING FUNCTION VIEWS - below

@api_view(['GET', 'POST'])
def article_list_apiview(request):
    if request.method == 'GET':
        # Fetch all Articles from the database
        articles = Article.objects.all()

        # convert the queryset article using serializer
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For getting a particular article using its id
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_apiview(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # convert the queryset article using serializer
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
