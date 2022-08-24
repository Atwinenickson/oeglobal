from django.core.management.base import BaseCommand
from django.utils import timezone

from oeglobal_api.usecases.savepodcast import OeglobalPodcast

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        OeglobalPodcast().OeglobalData()