from django.urls import include, path

from rest_framework import routers

from oeglobal_api.views import ArticleViewSet, TopicViewSet, TopicURLViewSet, PodcastViewSet, RecentPodcastViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topicsurl', TopicURLViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'recentpodcasts', RecentPodcastViewSet)

urlpatterns = [
   path('', include(router.urls)),
]