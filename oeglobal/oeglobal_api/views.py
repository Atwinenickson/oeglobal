from rest_framework import viewsets

from oeglobal_api.serializers import ArticleSerializer, TopicSerializer, TopicURLSerializer, PodcastSerializer, RecentPodcastSerializer
from oeglobal_api.models import Article, Topic, TopicURL, Podcast, RecentPodcast


class ArticleViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer


class TopicViewSet(viewsets.ModelViewSet):
   queryset = Topic.objects.all()
   serializer_class = TopicSerializer

class TopicURLViewSet(viewsets.ModelViewSet):
   queryset = TopicURL.objects.all()
   serializer_class = TopicURLSerializer

class PodcastViewSet(viewsets.ModelViewSet):
   queryset = Podcast.objects.all()
   serializer_class = PodcastSerializer


class RecentPodcastViewSet(viewsets.ModelViewSet):
   queryset = RecentPodcast.objects.all()
   serializer_class = RecentPodcastSerializer