from django.db import models


class Article(models.Model):
    title = models.TextField(max_length=300, null=True)
    url = models.URLField(max_length=300, null=True)
    replies = models.TextField(max_length=300, null=True)
    views = models.TextField(max_length=300, null=True)
    date = models.TextField(max_length=300, null=True)


class Topic(models.Model):
    topic = models.TextField(max_length=300, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class TopicURL(models.Model):
    url = models.URLField(max_length=300, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Podcast(models.Model):
    title = models.TextField(max_length=300, null=True)
    url = models.URLField(max_length=300, null=True)
    comments = models.TextField(max_length=300, null=True)
    description = models.TextField(max_length=300, null=True)
    date = models.TextField(max_length=300, null=True)


class RecentPodcast(models.Model):
    title = models.TextField(max_length=300, null=True)
    url = models.URLField(max_length=300, null=True)
    date = models.TextField(max_length=300, null=True)


class SinglePodcast(models.Model):
    title = models.TextField(max_length=300, null=True)
    audio_link = models.TextField(max_length=300, null=True)
    description = models.TextField(null=True)
    date = models.TextField(null=True)
