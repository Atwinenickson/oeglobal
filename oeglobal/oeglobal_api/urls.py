from django.urls import include, path

from rest_framework import routers

from oeglobal_api.views import ArticleViewSet, TopicViewSet, TopicURLViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topicsurl', TopicURLViewSet)

urlpatterns = [
   path('', include(router.urls)),
]