from rest_framework import serializers

from oeglobal_api.models import (
    Article,
    Topic,
    TopicURL,
    Podcast,
    RecentPodcast,
    SinglePodcast,
)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "url", "replies", "views", "date")


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("topic", "article")


class TopicURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicURL
        fields = ("url", "topic")


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ("title", "url", "comments", "description", "date")


class RecentPodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentPodcast
        fields = ("title", "url", "date")


class SinglePodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglePodcast
        fields = ("title", "audio_link", "description", "date")
