
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from ramenki.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from other import views as other_views
from static_pages import views as static_pages_views
from users import views as user_views

about_urls = (
    path("structure/", user_views.structure_view, name="about-structure"),
    path("legend/", user_views.veterans_view, name="about-veterans"),
    path("instructors/", user_views.instructors_view, name="about-instructors"),
    path("judiciary/", user_views.judiciary_view, name="about-judiciary"),
    path("", static_pages_views.about_static_page_view, name="main"),
    path("<str:page_url>/", static_pages_views.about_static_page_view, name="static-page"),
)

karate_urls = (
    path("attestation/", static_pages_views.attestation_view, name="attestation"),
    path("", static_pages_views.karate_static_page_view, name="main"),
    path("<str:page_url>/", static_pages_views.karate_static_page_view, name="static-page"),
)

taekwondo_urls = (
    path("instructors/", user_views.taekwondo_instructors_view, name="instructors"),
    path("", static_pages_views.taekwondo_static_page_view, name="main"),
    path("<str:page_url>/", static_pages_views.taekwondo_static_page_view, name="static-page"),
)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', other_views.index_view, name="index"),

    path('contacts/', other_views.contacts_view, name="contacts"),
    path('map-script/', other_views.map_script, name="map-script"),

    path('news/', include('news.urls'), name="news"),
    path('media/', include('mediacontent.urls'), name='mediacontent'),

    url('', include('social_django.urls', namespace='social')),
    path('', include('users.urls')),
    path('about/', include((about_urls, "about"))),
    path('karate/', include((karate_urls, "karate"))),
    path('taekwondo/', include((taekwondo_urls, "taekwondo"))),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = other_views.handler404
handler500 = other_views.handler500
