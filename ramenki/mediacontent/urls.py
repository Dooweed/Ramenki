from django.urls import path
from . import views

app_name = "mediacontent"

urlpatterns = [
    path("photos/<str:category>/", views.photos_view, name="photos"),
    path("photos/<str:category>/<int:page>", views.photos_view, name="photos-page"),
    path("videos/<str:category>/", views.videos_view, name="videos"),
    path("videos/<str:category>/<int:page>", views.videos_view, name="videos-page"),
    path("", views.main_view, name="main"),
    path("<int:page>", views.main_view, name="main-page"),
]
