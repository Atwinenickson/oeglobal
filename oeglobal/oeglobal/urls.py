from django.urls import path, include

urlpatterns = [
   path('articles/', include('oeglobal_api.urls')),
]