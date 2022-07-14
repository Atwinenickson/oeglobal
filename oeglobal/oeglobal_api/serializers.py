from rest_framework import serializers

from oeglobal_api.models import Article, Topic, TopicURL

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