from django.core.management.base import BaseCommand
from django.utils import timezone

from oeglobal_api.usecases.savearticles import OeglobalNewsDetail

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        OeglobalNewsDetail("https://connect.oeglobal.org/").OeglobalData()