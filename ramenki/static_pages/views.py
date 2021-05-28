from ramenki.utils import render_extended as render
from django.shortcuts import get_object_or_404, redirect
from news.models import Article
from django.http import Http404
from .models import *

# Create your views here.

def karate_static_page_view(request, page_url=""):
    subdivisions_list = KarateStaticPage.objects.filter(active=True)
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    page = subdivisions_list.filter(url=page_url)
    if page.exists():
        page = page.first()
    elif page_url == "":
        if subdivisions_list:
            page = subdivisions_list[0]
            return redirect("karate:static-page", page_url=page.url)
        else:
            raise Http404("Страница не существует")
    else:
        raise Http404("Страница не существует")

    subdivisions_list = subdivisions_list.exclude(url="")

    context = {
        "page": page,
        "subdivisions_list": subdivisions_list,
        "news": news,
    }
    return render(request, 'karate/static-page.html', context)

def taekwondo_static_page_view(request, page_url=""):
    subdivisions_list = TaekwondoStaticPage.objects.filter(active=True)
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    page = subdivisions_list.filter(url=page_url)
    if page.exists():
        page = page.first()
    elif page_url == "":
        if subdivisions_list:
            page = subdivisions_list[0]
            return redirect("taekwondo:static-page", page_url=page.url)
        else:
            raise Http404("Страница не существует")
    else:
        raise Http404("Страница не существует")

    subdivisions_list = subdivisions_list.exclude(url="")

    context = {
        "page": page,
        "subdivisions_list": subdivisions_list,
        "news": news,
    }
    return render(request, 'taekwondo/static-page.html', context)

def about_static_page_view(request, page_url=""):
    subdivisions_list = AboutStaticPage.objects.filter(active=True)
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    page = subdivisions_list.filter(url=page_url)
    if page.exists():
        page = page.first()
    elif page_url == "":
        if subdivisions_list:
            page = subdivisions_list[0]
            return redirect("about:static-page", page_url=page.url)
        else:
            raise Http404("Страница не существует")
    else:
        raise Http404("Страница не существует")

    subdivisions_list = subdivisions_list.exclude(url="")

    context = {
        "page": page,
        "subdivisions_list": subdivisions_list,
        "news": news,
    }
    return render(request, 'about/static-page.html', context)

def attestation_view(request):
    subdivisions_list = KarateStaticPage.objects.filter(active=True)
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    page = get_object_or_404(KarateStaticPage, url="attestation")

    border = page.content.index("<div class=\"belt__additional_content\">")

    belts = page.content[border:]
    belts = belts.split("<div class=\"belt__additional_content\">")
    belts = belts[1:]
    for n, i in enumerate(belts):
        belts[n] = i[:i.rfind("</div>")]
    page.content = page.content[:border]

    subdivisions_list = subdivisions_list.exclude(url="")

    context = {
        "page": page,
        "subdivisions_list": subdivisions_list,
        "belts": belts,
        "news": news,
    }
    return render(request, 'karate/attestation.html', context)
