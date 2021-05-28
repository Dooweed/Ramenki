from ramenki.utils import render_extended as render
from news.models import Article
from django.http import HttpResponse
from ramenki.utils import render_map_script
from mediacontent.views import last_media
from .models import City, SliderItem, Branch, MiniSliderItem
from .forms import CallbackForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index_view(request):
    news = Article.objects.filter(status='published').order_by("-date")[:5]
    slider_items = SliderItem.objects.filter(active=True).order_by("-sorting")
    mini_slider_items = MiniSliderItem.objects.filter(active=True).order_by("-sorting")

    context = {
        "news": news,
        "media": last_media(),
        "slider_items": slider_items,
        "mini_slider_items": mini_slider_items,
    }

    return render(request, "index.html", context)


def contacts_view(request):
    city_id, branch_id = None, None
    cities = City.objects.filter(branch__isnull=False).distinct()
    all_branches = Branch.objects.all()
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            branch = Branch.objects.get(id=form.data["branch_id"])
            send_mail(
                f"Сообщение из раздела \"Обратная связь\"",
                f'Имя: {form.cleaned_data["name"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Сообщение:\n{form.cleaned_data["message"]}',
                settings.DEFAULT_FROM_EMAIL,
                (branch.email, ),
                fail_silently=True
            )

            form = CallbackForm()
        else:
            city_id, branch_id = int(form.data["city_id"]), int(form.data["branch_id"])
    else:
        form = CallbackForm()

    context = {
        "cities": cities,
        "news": news,
        "form": form,
        "all_branches": all_branches,
        "city_id": city_id,
        "branch_id": branch_id,
    }
    return render(request, 'contacts/contacts.html',  context)

def map_script(request):
    cities = City.objects.filter(branch__isnull=False)
    return HttpResponse(render_map_script(cities), content_type="application/x-javascript")

def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
