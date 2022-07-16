from django.db import models


class Article(models.Model):
   ArticleID = models.TextField(max_length=300, null=True)
   Title = models.TextField(max_length=300, null=True)
   Articleurl = models.TextField(max_length=300, null=True)
   Replies = models.TextField(max_length=300, null=True)
   Views = models.TextField(max_length=300, null=True)
   Date = models.TextField(max_length=300, null=True)

class Topic(models.Model):
   TopicID = models.TextField(max_length=300, null=True)
   Topic = models.TextField(max_length=300, null=True)
   ArticleID = models.ForeignKey(Article, on_delete=models.CASCADE)

class TopicURL(models.Model):
   TopicUrlID = models.TextField(max_length=300, null=True)
   TopicUrl = models.TextField(max_length=300, null=True)
   TopicID = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Podcast(models.Model):
   # PodcastID = models.TextField(max_length=300, null=True)
   Title = models.TextField(max_length=300, null=True)
   Podcasturl = models.TextField(max_length=300, null=True)
   Comments = models.TextField(max_length=300, null=True)
   Description = models.TextField(max_length=300, null=True)
   Date = models.TextField(max_length=300, null=True)


class RecentPodcast(models.Model):
   # RecentPodcastID = models.TextField(max_length=300, null=True)
   Title = models.TextField(max_length=300, null=True)
   RecentPodcasturl = models.TextField(max_length=300, null=True)
   Date = models.TextField(max_length=300, null=True)


class SinglePodcast(models.Model):
   SinglePodcastID = models.TextField(max_length=300, null=True)
   Title = models.TextField(max_length=300, null=True)
   Audiolink = models.TextField(max_length=300, null=True)
   Description = models.TextField(null=True)
   Date = models.TextField(null=True)