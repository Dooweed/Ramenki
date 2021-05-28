from ramenki.utils import render_extended as render
from django.http import HttpResponseNotFound, Http404
from .models import ArticleCategory, Article
from math import ceil
from ramenki.static_vars import ARTICLES_PER_PAGE, ARCHIVING_DAYS_LIMIT, DEFAULT_ARTICLE_IMAGES, NEWS_BLOCK_DEFAULT_ARTICLE_IMAGES
from django.utils import timezone
from datetime import timedelta
from mediacontent.views import recent_media
from other.models import CeoSettings


# Create your views here.

def category_view(request, category='all', page=1):
    categories = ArticleCategory.objects.filter(active=True)
    category_object = categories.filter(url=category)
    all_meta_description = CeoSettings.objects.filter(template_name="news/news.html").first()
    if all_meta_description:
        all_meta_description = all_meta_description.meta_description if all_meta_description.meta_description else ""
    else:
        all_meta_description = ""
    if category == "all":
        meta_description = all_meta_description
        query_set = Article.objects.filter(date__lte=timezone.now(), date__gt=timezone.now() - timedelta(days=ARCHIVING_DAYS_LIMIT),
                                           status='published').order_by("-date")
        pages_count = ceil(query_set.count() / ARTICLES_PER_PAGE)
        query_set = query_set[(page - 1) * ARTICLES_PER_PAGE:ARTICLES_PER_PAGE * page]
    elif category == "archive":
        meta_description = "Архив новостей СК Раменки."
        query_set = Article.objects.filter(date__lte=timezone.now() - timedelta(days=ARCHIVING_DAYS_LIMIT), status='published').order_by("-date")
        pages_count = ceil(query_set.count() / ARTICLES_PER_PAGE)
        query_set = query_set[(page - 1) * ARTICLES_PER_PAGE:ARTICLES_PER_PAGE * page]
    elif category_object.exists():
        category_object = category_object[0]
        meta_description = category_object.meta_description if category_object.meta_description else all_meta_description
        query_set = Article.objects.filter(associations=category_object, status='published').order_by("-date")
        pages_count = ceil(query_set.count() / ARTICLES_PER_PAGE)
        query_set = query_set[(page - 1) * ARTICLES_PER_PAGE:ARTICLES_PER_PAGE * page]
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
        obj.description, obj.default_thumb = obj.description(), DEFAULT_ARTICLE_IMAGES[i]

    request.session['last_category'] = category

    if category == "all":
        verbose_category = "Все"
    elif category == "archive":
        verbose_category = "Архив"
    else:
        verbose_category = category_object.name
    title = f"Новости: {verbose_category}"

    context = {
        "pages_count": pages_count,
        "current_page": page,
        "prev_page": prev_page,
        "next_page": next_page,
        "query_set": query_set,
        "categories": categories,
        "current_category_url": category,
        "title": title,
        "media": recent_media(),
        "meta_description": meta_description,
    }

    return render(request, "news/news.html", context)


def article_view(request, article_url):
    article = Article.objects.filter(url=article_url, status="published")
    if article.exists():
        article = article[0]
    else:
        return HttpResponseNotFound("Данной страницы не существует")

    other_news = Article.objects.filter(status='published').order_by("-date")[:5]
    if other_news.exists():
        other_news = list(other_news)
        if article in other_news:
            other_news.remove(article)
        else:
            other_news = other_news[:4]
    for i, obj in enumerate(other_news):
        obj.description, obj.default_thumb = obj.description(), NEWS_BLOCK_DEFAULT_ARTICLE_IMAGES[i]

    if 'last_category' in request.session:
        last_category = request.session['last_category']
        if last_category != 'all' and last_category != 'archive':
            next_article = Article.objects.filter(date__gt=article.date, status="published", associations__url=last_category)
        else:
            next_article = Article.objects.filter(date__gt=article.date, status="published")
    else:
        last_category = 'all'
        next_article = Article.objects.filter(date__gt=article.date, status="published")

    if next_article.exists():
        next_article = next_article.first()
        next_article.date_string = next_article.date_string()
    else:
        next_article = None

    title = article.title

    context = {
        "article": article,
        "next_article": next_article,
        "other_news": other_news,
        "last_category": last_category,
        "media": recent_media(),
        "title": title,
    }

    return render(request, "news/article.html", context)
