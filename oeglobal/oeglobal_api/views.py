from rest_framework import viewsets
from rest_framework import filters

from oeglobal_api.serializers import (
    ArticleSerializer,
    TopicSerializer,
    TopicURLSerializer,
    PodcastSerializer,
    RecentPodcastSerializer,
    SinglePodcastSerializer,
)
from oeglobal_api.models import (
    Article,
    Topic,
    TopicURL,
    Podcast,
    RecentPodcast,
    SinglePodcast,
)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        "title",
        "url",
        "replies",
        "views",
        "date",
    ]
    search_fields = ["title", "url", "replies", "views", "date"]
    ordering_fields = "__all__"


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["topic", "article"]
    search_fields = ["topic", "article"]
    ordering_fields = "__all__"


class TopicURLViewSet(viewsets.ModelViewSet):
    queryset = TopicURL.objects.all()
    serializer_class = TopicURLSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["url", "topic"]
    search_fields = ["url", "topic"]
    ordering_fields = "__all__"


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title", "url", "comments", "description", "date"]
    search_fields = ["title", "url", "comments", "description", "date"]
    ordering_fields = "__all__"


class RecentPodcastViewSet(viewsets.ModelViewSet):
    queryset = RecentPodcast.objects.all()
    serializer_class = RecentPodcastSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title", "url", "date"]
    search_fields = ["title", "url", "date"]
    ordering_fields = "__all__"


class SinglePodcastViewSet(viewsets.ModelViewSet):
    queryset = SinglePodcast.objects.all()
    serializer_class = SinglePodcastSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        "title",
        "audio_link",
        "description",
        "date",
    ]
    search_fields = ["title", "audio_link", "description", "date"]
    ordering_fields = "__all__"
