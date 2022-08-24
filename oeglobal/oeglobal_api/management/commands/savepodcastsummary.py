from django.core.management.base import BaseCommand
from django.utils import timezone

from oeglobal_api.usecases.savepodcastsummary import OeglobalPodcastDetail

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        OeglobalPodcastDetail("https://podcast.oeglobal.org/").OeglobalData()




