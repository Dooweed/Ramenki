from .static_vars import RESERVED_CATEGORIES
from django.templatetags.static import static
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render

def category_url_validator(value):
    if value in RESERVED_CATEGORIES:
        raise ValidationError("Данный URL зарезервирован другой категорией")

def render_extended(request, template_name, context=None, content_type=None, status=None, using=None):
    context["template_name"] = template_name
    return render(request, template_name, context, content_type, status, using)


def paired_range(start, stop):
    pairs = []
    for n in range(start, stop):
        pairs.append((n, n))
    return tuple(pairs)

def link_tag(url, name=None, classes=None):
    if not name:
        name = url
    return f"""<a href="{url}"{"" if not classes else " ".join(classes)}>{name}</a>"""

def make_link(url, classes=None, name=None):
    val = URLValidator()
    try:
        val(url)
        return link_tag(url, classes, name)
    except ValidationError:
        return url

def get_ending(number, options):
    if len(options) != 3:
        return "Ошибка"
    number = str(number)
    last_char = int(number[-1:])
    if last_char == 1 and number[-2:] != '11':
        return f"{number} {options[0]}"
    elif 2 <= last_char <= 4 and number[-2:] != "12" and number[-2:] != "13" and number[-2:] != "14":
        return f"{number} {options[1]}"
    else:
        return f"{number} {options[2]}"

def get_placemark(city_id, branch_id, branch_lat, branch_lon, branch_title):
    return f"""
            placemark{city_id}_{branch_id} = new ymaps.Placemark([{branch_lat}, {branch_lon}],
            {{
                hintContent: '{branch_title}',
            }}, {{
                iconLayout: imageStaticLayout,
                iconImageHref: imageStaticHref,
                iconImageSize: imageStaticSize,
                iconImageOffset: imageStaticOffset
            }}), """

def get_placemark_event(city_id, branch_id, unfilled_city_id, unfilled_branch_id, branch_lat, branch_lon):
    return f"""placemark{city_id}_{branch_id}.events.add('click', function (e) {{
                var coords = [{branch_lat}, {branch_lon}];
                var map = e.get('map')
                map.setZoom(18, {{"smooth": true}});
                map.panTo(coords, {{"flying": true}});
                let element = document.querySelectorAll('[data-target="address-{unfilled_city_id}_{unfilled_branch_id}"]');
                if (element){{ 
                    element[0].click(); 
                }}
            }});\n"""

def render_map_script(city):
    general = ""
    all_placemarks = ""
    all_placemark_events = ""
    all_geo_objects = ""
    JS_STATIC_VARS = f"""const imageStaticHref = "{static('img/map-point.png')}",
                               imageStaticSize = [106, 111],
                               imageStaticOffset = [-53, -111],
                               imageStaticLayout = 'default#image';
                            """
    lat_sum = 0
    lon_sum = 0
    iterations = 0
    for city in cities:
        placemarks = ""
        placemark_events = ""
        geo_objects = ""
        city_lat_sum = 0
        city_lon_sum = 0
        city_iterations = 0
        for branch in city.branch_set.all():
            branch_id = branch.filled_id()
            city_id = city.filled_id()
            branch_title = branch.title()
            placemarks += get_placemark(city_id, branch_id, branch.geocode_lat, branch.geocode_lon, branch_title)
            placemark_events += get_placemark_event(city_id, branch_id, city.id, branch.id, branch.geocode_lat, branch.geocode_lon)
            all_placemarks += get_placemark(99, branch_id, branch.geocode_lat, branch.geocode_lon, branch_title)
            all_placemark_events += get_placemark_event(99, branch_id, 99, branch.id, branch.geocode_lat, branch.geocode_lon)

            geo_objects += f".add(placemark{city_id}_{branch_id})"
            all_geo_objects += f".add(placemark{99}_{branch_id})"
            city_lat_sum += branch.geocode_lat
            city_lon_sum += branch.geocode_lon
            city_iterations += 1

        lat_sum += city_lat_sum
        lon_sum += city_lon_sum
        iterations += city_iterations

        placemarks = f"{placemarks[:placemarks.rfind(',')]};{placemarks[:placemarks.rfind(',') + 1]}"

        general += f"""
            var map{city.filled_id()} = new ymaps.Map('map-{city.filled_id()}', {{
                  center: [{city_lat_sum/city_iterations}, {city_lon_sum/city_iterations}],
                  zoom: 11
              }}),

            {placemarks}

            {placemark_events}

            map{city.filled_id()}.geoObjects{geo_objects}; """

    # All placemarks
    all_placemarks = f"{all_placemarks[:all_placemarks.rfind(',')]};{all_placemarks[:all_placemarks.rfind(',') + 1]}"

    general = f"""
        var map{99} = new ymaps.Map('map-{99}', {{
              center: [{lat_sum/iterations}, {lon_sum/iterations}],
              zoom: 4
          }}),

        {all_placemarks}

        {all_placemark_events}

        map{99}.geoObjects{all_geo_objects}; 

        {general}"""

    return f"{JS_STATIC_VARS}\n\nymaps.ready(function () {{ {general} }});"
