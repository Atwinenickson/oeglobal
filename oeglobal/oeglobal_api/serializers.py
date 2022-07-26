from rest_framework import serializers

from oeglobal_api.models import Article, Topic, TopicURL, Podcast, RecentPodcast, SinglePodcast

class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = ('article_id', 'title', 'article_url', 'replies', 'views', 'date')
       


class TopicSerializer(serializers.ModelSerializer):
   class Meta:
       model = Topic
       fields = ('topic_id', 'topic', 'article_id')

class TopicURLSerializer(serializers.ModelSerializer):
   class Meta:
       model = TopicURL
       fields = ('topic_url_id', 'topic_url', 'topic_id')

class PodcastSerializer(serializers.ModelSerializer):
   class Meta:
       model = Podcast
       fields = ('title', 'podcast_url', 'comments', 'description', 'date')

class RecentPodcastSerializer(serializers.ModelSerializer):
   class Meta:
       model = RecentPodcast
       fields = ('title', 'recent_podcast_url', 'date')

class SinglePodcastSerializer(serializers.ModelSerializer):
   class Meta:
       model = SinglePodcast
       fields = ('single_podcast_id','title',  'audio_link', 'description', 'date')