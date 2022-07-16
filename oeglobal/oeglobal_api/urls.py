from django.urls import include, path

from rest_framework import routers

from oeglobal_api.views import ArticleViewSet, TopicViewSet, TopicURLViewSet, PodcastViewSet, RecentPodcastViewSet, SinglePodcastViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topicsurl', TopicURLViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'recentpodcasts', RecentPodcastViewSet)
router.register(r'singlepodcast', SinglePodcastViewSet) 

urlpatterns = [
   path('', include(router.urls)),
]