from django.urls import path, include

urlpatterns = [
    path("oeglobal/", include("oeglobal_api.urls")),
]
