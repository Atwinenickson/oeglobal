from rest_framework import viewsets

from oeglobal_api.serializers import ArticleSerializer
from oeglobal_api.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer