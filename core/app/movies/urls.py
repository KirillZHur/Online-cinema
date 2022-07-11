from django.urls import path, include
from .views import index_page, info_page, player

urlpatterns = [
    path('', index_page),
    path('about-us', info_page),
    path('movies/<str:name>', player)
]

