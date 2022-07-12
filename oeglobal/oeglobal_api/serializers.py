from rest_framework import serializers

from oeglobal_api.models import Article

class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = ('title', 'year_created', 'author', 'description')
