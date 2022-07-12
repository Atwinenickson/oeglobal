from django.urls import include, path

from rest_framework import routers

from oeglobal_api.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
   path('', include(router.urls)),
]