from datetime import datetime

def safe_extract(dictionary, key):
    try:
        return dictionary[key]
    except:
        return

def fill_user_profile(response, *args, **kwargs):
    try:
        user = kwargs.get("user")
    except:
        return
    try:
        email = safe_extract(response, "email")
        if email:
            user.email = email
    except:
        pass
    forename = safe_extract(response, "first_name")
    if forename:
        user.forename = forename
    user.surname = safe_extract(response, "last_name")
    user.phone = safe_extract(response, "phone")
    has_photo = safe_extract(response, "has_photo")
    user.profile.use_social_photo = has_photo
    if has_photo:
        user.profile.social_avatar = safe_extract(response, "photo_50")
        user.profile.social_photo = safe_extract(response, "photo_max_orig")
    bdate = safe_extract(response, "bdate")
    if bdate:
        if len(bdate) > 5:
            user.profile.birth_date = datetime.strptime(bdate, '%d.%m.%Y')
        else:
            user.profile.birth_date = datetime.strptime(bdate, '%d.%m')
    user.save()
    user.profile.save()
