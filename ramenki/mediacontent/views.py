from ramenki.utils import render_extended as render
from ramenki.static_vars import MEDIA_PER_PAGE, GALLERIES_PER_PAGE, VIDEOS_PER_PAGE, DEFAULT_MEDIA_IMAGES
from django.http import Http404
from math import ceil
from news.models import Article
from .models import *
from other.models import CeoSettings

# Create your views here.

def recent_media():
    videos = Video.objects.all().order_by("-date").first()
    galleries = PhotoGallery.objects.all().order_by("-date")[:3]

    if not videos and not galleries:
        return None

    if videos:
        videos.default_thumb = DEFAULT_MEDIA_IMAGES[0]
    if not galleries:
        return videos, None
    for i, obj in enumerate(galleries):
        obj.default_thumb = DEFAULT_MEDIA_IMAGES[i+1]

    return videos, list(galleries)

def last_media():
    video = Video.objects.all().order_by("-date").first()
    gallery = PhotoGallery.objects.all().order_by("-date").first()
    if not video and not gallery:
        return None
    if video:
        video.video, video.default_thumb = True, DEFAULT_MEDIA_IMAGES[0]
    if gallery:
        gallery.video, gallery.default_thumb = False, DEFAULT_MEDIA_IMAGES[0]
    if not video:
        return gallery
    if not gallery:
        return video
    return video if video.date > gallery.date else gallery


def main_view(request, page=1):
    galleries = PhotoGallery.objects.all()
    videos = Video.objects.all()
    pages_count = galleries.count() + videos.count()

    pages_count = ceil(pages_count / MEDIA_PER_PAGE)

    if page > pages_count and page != 1:
        raise Http404

    videos = list(videos.order_by("date")[(page - 1) * MEDIA_PER_PAGE: MEDIA_PER_PAGE * page])
    galleries = list(galleries.order_by("date")[(page - 1) * MEDIA_PER_PAGE: MEDIA_PER_PAGE * page])
    query_set = []
    for i in range(0, MEDIA_PER_PAGE):
        if galleries and videos:
            if galleries and galleries[0].date > videos[0].date:
                obj = galleries.pop(0)
                obj.gallery = True
                query_set.append(obj)
            else:
                obj = videos.pop(0)
                obj.gallery = False
                query_set.append(obj)
        else:
            if galleries:
                obj = galleries.pop(0)
                obj.gallery = True
                query_set.append(obj)
            elif videos:
                obj = videos.pop(0)
                obj.videos = True
                query_set.append(obj)
            else:
                break

    prev_page, next_page = page, page
    if not page == 1:
        prev_page = page - 1
    if not page == pages_count:
        next_page = page + 1

    if pages_count == 1:
        pages_count = (1,)
    else:
        pages_count = range(1, pages_count + 1)

    for i, obj in enumerate(query_set):
        obj.default_thumb = DEFAULT_MEDIA_IMAGES[i]

    news = Article.objects.filter(status='published').order_by("-date")[:4]

    context = {
        "pages_count": pages_count,
        "current_page": page,
        "prev_page": prev_page,
        "next_page": next_page,
        "query_set": query_set,
        "news": news,
        "title": "Медиа",
    }

    return render(request, 'media/media.html', context)

def photos_view(request, category, page=1):
    categories = MediaCategory.objects.filter(active=True, photogallery__isnull=False).distinct()
    category_object = categories.filter(url=category)
    all_meta_description = CeoSettings.objects.filter(template_name="media/media-category-photos.html").first()
    if all_meta_description:
        all_meta_description = all_meta_description.meta_description if all_meta_description.meta_description else ""
    else:
        all_meta_description = ""
    if category == "all":
        query_set = PhotoGallery.objects.all().order_by("-date")
        meta_description = "Фото галерея жизни клуба СК Раменки."
        category_name = "Все"
        pages_count = ceil(query_set.count() / GALLERIES_PER_PAGE)
        query_set = query_set[(page - 1) * GALLERIES_PER_PAGE:GALLERIES_PER_PAGE * page]
    elif category_object.exists():
        category_object = category_object[0]
        meta_description = category_object.meta_description if category_object.meta_description else all_meta_description
        category_name = category_object.name
        query_set = PhotoGallery.objects.filter(category=category_object).order_by("-date")
        pages_count = ceil(query_set.count() / GALLERIES_PER_PAGE)
        query_set = query_set[(page - 1) * GALLERIES_PER_PAGE:GALLERIES_PER_PAGE * page]
    else:
        raise Http404

    if page > pages_count and page != 1:
        raise Http404

    prev_page, next_page = page, page
    if not page == 1:
        prev_page = page - 1
    if not page == pages_count:
        next_page = page + 1

    if pages_count == 1:
        pages_count = (1,)
    else:
        pages_count = range(1, pages_count + 1)

    for i, obj in enumerate(query_set):
        obj.default_thumb = DEFAULT_MEDIA_IMAGES[i]

    news = Article.objects.filter(status='published').order_by("-date")[:4]

    context = {
        "pages_count": pages_count,
        "current_page": page,
        "prev_page": prev_page,
        "next_page": next_page,
        "query_set": query_set,
        "categories": categories,
        "current_category_name": category_name,
        "current_category_url": category,
        "news": news,
        "title": f"Фото — {category_name}",
        "meta_description": meta_description,
    }

    return render(request, "media/media-category-photos.html", context)

def videos_view(request, category, page=1):
    categories = MediaCategory.objects.filter(active=True, video__isnull=False).distinct()
    category_object = categories.filter(url=category)
    all_meta_description = CeoSettings.objects.filter(template_name="media/media-category-videos.html").first()
    if all_meta_description:
        all_meta_description = all_meta_description.meta_description if all_meta_description.meta_description else ""
    else:
        all_meta_description = ""
    if category == "all":
        query_set = Video.objects.all().order_by("-date")
        meta_description = "Видео галерея жизни клуба СК Раменки."
        category_name = "Все"
        pages_count = ceil(query_set.count() / VIDEOS_PER_PAGE)
        query_set = query_set[(page - 1) * VIDEOS_PER_PAGE:VIDEOS_PER_PAGE * page]
    elif category_object.exists():
        category_object = category_object[0]
        meta_description = category_object.meta_description if category_object.meta_description else all_meta_description
        category_name = category_object.name
        query_set = Video.objects.filter(category=category_object).order_by("-date")
        pages_count = ceil(query_set.count() / VIDEOS_PER_PAGE)
        query_set = query_set[(page - 1) * VIDEOS_PER_PAGE:VIDEOS_PER_PAGE * page]
    else:
        raise Http404

    if page > pages_count and page != 1:
        raise Http404

    prev_page, next_page = page, page
    if not page == 1:
        prev_page = page - 1
    if not page == pages_count:
        next_page = page + 1

    if pages_count == 1:
        pages_count = (1,)
    else:
        pages_count = range(1, pages_count + 1)

    for i, obj in enumerate(query_set):
        obj.default_thumb = DEFAULT_MEDIA_IMAGES[i]

    news = Article.objects.filter(status='published').order_by("-date")[:4]

    context = {
        "pages_count": pages_count,
        "current_page": page,
        "prev_page": prev_page,
        "next_page": next_page,
        "query_set": query_set,
        "categories": categories,
        "current_category_name": category_name,
        "current_category_url": category,
        "news": news,
        "title": f"Видео — {category_name}",
        "meta_description": meta_description,
    }

    return render(request, "media/media-category-videos.html", context)
