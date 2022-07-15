from rest_framework import viewsets
from rest_framework import filters

from oeglobal_api.serializers import ArticleSerializer, TopicSerializer, TopicURLSerializer, PodcastSerializer, RecentPodcastSerializer
from oeglobal_api.models import Article, Topic, TopicURL, Podcast, RecentPodcast


class ArticleViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['ArticleID', 'Title', 'Articleurl', 'Replies', 'Views', 'Date']
   filter_backends = [filters.OrderingFilter]
   ordering_fields = '__all__'


class TopicViewSet(viewsets.ModelViewSet):
   queryset = Topic.objects.all()
   serializer_class = TopicSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['TopicID', 'Topic', 'ArticleID']
   filter_backends = [filters.OrderingFilter]
   ordering_fields = '__all__'

class TopicURLViewSet(viewsets.ModelViewSet):
   queryset = TopicURL.objects.all()
   serializer_class = TopicURLSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['TopicUrlID', 'TopicUrl', 'TopicID']
   filter_backends = [filters.OrderingFilter]
   ordering_fields = '__all__'

class PodcastViewSet(viewsets.ModelViewSet):
   queryset = Podcast.objects.all()
   serializer_class = PodcastSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['Title', 'Podcasturl', 'Comments', 'Description', 'Date']
   filter_backends = [filters.OrderingFilter]
   ordering_fields = '__all__'


class RecentPodcastViewSet(viewsets.ModelViewSet):
   queryset = RecentPodcast.objects.all()
   serializer_class = RecentPodcastSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['Title', 'RecentPodcasturl', 'Date']
   filter_backends = [filters.OrderingFilter]
   ordering_fields = '__all__'