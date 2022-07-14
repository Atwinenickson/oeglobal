from rest_framework import serializers

from oeglobal_api.models import Article, Topic, TopicURL, Podcast, RecentPodcast

class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = ('ArticleID', 'Title', 'Articleurl', 'Replies', 'Views', 'Date')


class TopicSerializer(serializers.ModelSerializer):
   class Meta:
       model = Topic
       fields = ('TopicID', 'Topic', 'ArticleID')

class TopicURLSerializer(serializers.ModelSerializer):
   class Meta:
       model = TopicURL
       fields = ('TopicUrlID', 'TopicUrl', 'TopicID')

class PodcastSerializer(serializers.ModelSerializer):
   class Meta:
       model = Podcast
       fields = ('Title', 'Podcasturl', 'Comments', 'Description', 'Date')

class RecentPodcastSerializer(serializers.ModelSerializer):
   class Meta:
       model = RecentPodcast
       fields = ('Title', 'RecentPodcasturl', 'Date')