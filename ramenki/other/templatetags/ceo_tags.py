from django import template
from other.models import CeoSettings, Settings

register = template.Library()

@register.simple_tag
def get_title(template_name, custom_title=None):
    obj = CeoSettings.objects.filter(template_name=template_name).first()
    if not obj:
        obj = CeoSettings.objects.filter(template_name="base.html").first()
    if obj.title_postfix:
        postfix = Settings.objects.filter(key="TITLE_POSTFIX").first()
        postfix = postfix.value
        if not obj.title and custom_title:
            obj.title = custom_title
        return f"{obj.title if obj.title else ''}{postfix if postfix else ''}"
    else:
        if not obj.title and custom_title:
            obj.title = custom_title
        return obj.title if obj.title else ""

@register.simple_tag
def get_meta_description(template_name):
    obj = CeoSettings.objects.filter(template_name=template_name).first()
    if not obj:
        obj = CeoSettings.objects.filter(template_name="base.html").first()
    meta = obj.meta_description if obj.meta_description else ""
    return meta

@register.simple_tag
def get_meta_keywords(template_name):
    obj = CeoSettings.objects.filter(template_name=template_name).first()
    if not obj:
        obj = CeoSettings.objects.filter(template_name="base.html").first()
    meta = obj.meta_keywords if obj.meta_keywords else ""
    return meta

@register.simple_tag
def get_meta_robots(template_name):
    obj = CeoSettings.objects.filter(template_name=template_name).first()
    if not obj:
        obj = CeoSettings.objects.filter(template_name="base.html").first()
    meta = obj.meta_robots if obj.meta_robots else ""
    return meta
