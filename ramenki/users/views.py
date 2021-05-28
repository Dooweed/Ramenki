from ramenki.utils import render_extended as render
from django.shortcuts import redirect, get_object_or_404
from news.models import Article
from .models import Staff, CustomUser, Profile
from .forms import RegisterForm, LoginForm, EditCustomUserForm, EditProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib.auth.forms import SetPasswordForm
from static_pages.models import TaekwondoStaticPage, AboutStaticPage


# Create your views here.

# About
def structure_view(request):
    CURRENT_PAGE_URL = "structure"
    subdivisions_list = AboutStaticPage.objects.filter(active=True)
    page = get_object_or_404(AboutStaticPage, url=CURRENT_PAGE_URL, active=True)
    page_content = page.content.split("<div class=\"about__text\">")
    page_content = page_content[1:]
    for n, i in enumerate(page_content):
        page_content[n] = i[:i.rfind("</div>")]

    president = Staff.objects.filter(active=True, position__contains="head-president").order_by("sorting").first()
    vice_president = Staff.objects.filter(active=True, position__contains="vice-president").order_by("sorting").first()

    coach_committee = Staff.objects.filter(active=True, position__contains="coach-committee").order_by("sorting")
    judiciary = Staff.objects.filter(active=True, position__contains="judiciary").order_by("sorting")
    methodical_certification_committee = Staff.objects.filter(active=True, position__contains="methodical-certification-committee").order_by("sorting")
    physical_mass_committee = Staff.objects.filter(active=True, position__contains="physical-mass-committee").order_by("sorting")
    administration = Staff.objects.filter(active=True, position__contains="administration").order_by("sorting")

    for section in (coach_committee, judiciary, methodical_certification_committee, physical_mass_committee, administration):
        num = 1
        for item in section:
            if num == 1:
                item.color_class = "person--red"
                num += 1
            elif num == 2:
                item.color_class = "person--black"
                num += 1
            else:
                item.color_class = ""
                num = 1

    news = Article.objects.filter(status='published').order_by("-date")[:4]

    subdivisions_list = subdivisions_list.exclude(url="")
    context = {
        "president": president,
        "vice_president": vice_president,
        "coach_committee": coach_committee,
        "judiciary": judiciary,
        "methodical_certification_committee": methodical_certification_committee,
        "physical_mass_committee": physical_mass_committee,
        "administration": administration,
        "news": news,
        "subdivisions_list": subdivisions_list,
        "page": page,
        "page_content": page_content,
    }

    return render(request, "about/structure.html", context)


def veterans_view(request):
    CURRENT_PAGE_URL = "legend"
    subdivisions_list = AboutStaticPage.objects.filter(active=True)
    page = get_object_or_404(AboutStaticPage, url=CURRENT_PAGE_URL, active=True)

    veterans = Staff.objects.filter(active=True, veteran=True).order_by("sorting")
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    subdivisions_list = subdivisions_list.exclude(url="")
    return render(request, 'about/veterans.html', {"veterans": veterans, "news": news, "subdivisions_list": subdivisions_list, "page": page})


def instructors_view(request):
    CURRENT_PAGE_URL = "instructors"
    subdivisions_list = AboutStaticPage.objects.filter(active=True)
    page = get_object_or_404(AboutStaticPage, url=CURRENT_PAGE_URL, active=True)

    instructors = Staff.objects.filter(active=True, position__contains="single-coach")
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    subdivisions_list = subdivisions_list.exclude(url="")
    return render(request, 'about/instructors.html', {"instructors": instructors, "news": news, "subdivisions_list": subdivisions_list, "page": page})


def judiciary_view(request):
    CURRENT_PAGE_URL = "judiciary"
    subdivisions_list = AboutStaticPage.objects.filter(active=True)
    page = get_object_or_404(AboutStaticPage, url=CURRENT_PAGE_URL, active=True)

    judiciary = Staff.objects.filter(active=True, position__contains="judiciary")
    news = Article.objects.filter(status='published').order_by("-date")[:4]

    num = 1
    for item in judiciary:
        if num == 1:
            item.color_class = "person--red"
            num += 1
        elif num == 2:
            item.color_class = "person--black"
            num += 1
        else:
            item.color_class = ""
            num = 1

    subdivisions_list = subdivisions_list.exclude(url="")
    return render(request, 'about/judiciary.html', {"judiciary": judiciary, "news": news, "subdivisions_list": subdivisions_list, "page": page})


def taekwondo_instructors_view(request):
    CURRENT_PAGE_URL = "instructors"
    news = Article.objects.filter(status='published').order_by("-date")[:4]
    subdivisions_list = TaekwondoStaticPage.objects.filter(active=True)
    page = get_object_or_404(TaekwondoStaticPage, url=CURRENT_PAGE_URL, active=True)
    instructors = Staff.objects.filter(active=True, sports_kind__contains="taekwondo", position__contains="single-coach").order_by("sorting")
    subdivisions_list = subdivisions_list.exclude(url="")
    return render(request, 'taekwondo/instructors.html', {"news": news, "instructors": instructors, "subdivisions_list": subdivisions_list, "page": page})


# Auth
def register_view(request):
    if request.user.is_authenticated:
        return redirect("auth:profile")
    else:
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = CustomUser.objects.create_user(forename=register_form.cleaned_data["forename"], email=register_form.cleaned_data["email"],
                                                      phone=register_form.cleaned_data["phone"], password=register_form.cleaned_data["password"],
                                                      surname=register_form.cleaned_data["surname"])
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect("auth:profile")
        else:
            register_form = RegisterForm()

        login_form = LoginForm()

        return render(request, 'auth/auth.html', {"register_form": register_form, "login_form": login_form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("auth:profile")
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(request, email=login_form.cleaned_data["email"], password=login_form.cleaned_data["password"])
                if user:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect("auth:profile")
                else:
                    login_form.login_failed = True
        else:
            login_form = LoginForm()

        register_form = RegisterForm()

        return render(request, 'auth/auth.html', {"register_form": register_form, "login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("auth:login")


@login_required
def set_password_view(request):
    user = get_user(request)
    if user.has_usable_password():
        return redirect("auth:profile")
    if not user.email:
        context = {"title": "Личный кабинет",
                   "header": "Создание пароля",
                   "message": "Для создания пароля необходимо заполнить поле Email",
                   "profile_link": True, "profile_edit_link": True}
        return render(request, 'info_response.html', context)
    if request.method == "POST":
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {"title": "Личный кабинет",
                       "header": "Создание пароля",
                       "message": "<b>Пароль был успешно создан!</b><br>Теперь вы можете войти в ваш аккаунт, введя Email и пароль",
                       "profile_link": True}
            return render(request, 'info_response.html', context)
    else:
        form = SetPasswordForm(user=user)
    return render(request, "auth/password_reset/password_reset_confirm.html", {"form": form})


@login_required
def profile_view(request):
    user = get_user(request)
    profile = Profile.objects.filter(user=user).first()

    return render(request, 'auth/personal_area.html', {"profile": profile})


@login_required
def profile_edit_view(request):
    user = get_user(request)
    profile = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        user_form = EditCustomUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("auth:profile")
    else:
        user_form = EditCustomUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    return render(request, 'auth/edit_personal_area.html', {"user_form": user_form, "profile_form": profile_form})
