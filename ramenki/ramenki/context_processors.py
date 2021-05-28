def links(request):
    from other.models import Settings
    settings = Settings.objects.all()

    TITLE_POSTFIX = settings.filter(key="TITLE_POSTFIX").first()
    TITLE_POSTFIX = TITLE_POSTFIX.value if TITLE_POSTFIX else ""
    YOUTUBE_LINK = settings.filter(key="YOUTUBE_LINK").first()
    YOUTUBE_LINK = YOUTUBE_LINK.value if YOUTUBE_LINK else None
    INSTAGRAM_LINK = settings.filter(key="INSTAGRAM_LINK").first()
    INSTAGRAM_LINK = INSTAGRAM_LINK.value if INSTAGRAM_LINK else None
    FACEBOOK_LINK = settings.filter(key="FACEBOOK_LINK").first()
    FACEBOOK_LINK = FACEBOOK_LINK.value if FACEBOOK_LINK else None
    VK_LINK = settings.filter(key="VK_LINK").first()
    VK_LINK = VK_LINK.value if VK_LINK else None
    PHONE = settings.filter(key="PHONE").first()
    PHONE = PHONE.value if PHONE else None
    EMAIL = settings.filter(key="EMAIL").first()
    EMAIL = EMAIL.value if EMAIL else None
    PHONE_CITY = settings.filter(key="PHONE_CITY").first()
    PHONE_CITY = PHONE_CITY.value if PHONE_CITY else None
    return {"youtube_link": YOUTUBE_LINK, "instagram_link": INSTAGRAM_LINK, "facebook_link": FACEBOOK_LINK,
            "vk_link": VK_LINK, "phone": PHONE, "email": EMAIL, "phone_city": PHONE_CITY, "title_postfix": TITLE_POSTFIX}
