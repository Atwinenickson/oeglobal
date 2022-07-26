from django.db import models


class Article(models.Model):
   article_id = models.TextField(max_length=300, null=True)
   title = models.TextField(max_length=300, null=True)
   article_url = models.TextField(max_length=300, null=True)
   replies = models.TextField(max_length=300, null=True)
   views = models.TextField(max_length=300, null=True)
   date = models.TextField(max_length=300, null=True)

class Topic(models.Model):
   topic_id = models.TextField(max_length=300, null=True)
   topic = models.TextField(max_length=300, null=True)
   article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

class TopicURL(models.Model):
   topic_url_id = models.TextField(max_length=300, null=True)
   topic_url = models.TextField(max_length=300, null=True)
   topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Podcast(models.Model):
   # PodcastID = models.TextField(max_length=300, null=True)
   title = models.TextField(max_length=300, null=True)
   podcast_url = models.TextField(max_length=300, null=True)
   comments = models.TextField(max_length=300, null=True)
   description = models.TextField(max_length=300, null=True)
   date = models.TextField(max_length=300, null=True)


class RecentPodcast(models.Model):
   # RecentPodcastID = models.TextField(max_length=300, null=True)
   title = models.TextField(max_length=300, null=True)
   recent_podcast_url = models.TextField(max_length=300, null=True)
   date = models.TextField(max_length=300, null=True)


class SinglePodcast(models.Model):
   single_podcast_id = models.TextField(max_length=300, null=True)
   title = models.TextField(max_length=300, null=True)
   audio_link = models.TextField(max_length=300, null=True)
   description = models.TextField(null=True)
   date = models.TextField(null=True)