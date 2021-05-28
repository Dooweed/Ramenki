from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("article/<str:article_url>/", views.article_view, name="article"),
    path("", views.category_view, name="news"),
    path("<str:category>/", views.category_view, name="category"),
    path("<str:category>/<int:page>/", views.category_view, name="category-page"),
]
