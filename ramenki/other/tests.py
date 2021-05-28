from django.test import TestCase

# Create your tests here.

import requests
import json
from .models import MetroStation

response = requests.get("https://api.hh.ru/metro/1")
response = json.loads(response.content)

created = 0
changed = 0

for line in response['lines']:
    for station in line['stations']:
        obj = MetroStation.objects.filter(station_name=station['name'], line_name=line['name'])
        if obj.exists():
            obj = obj[0]
            is_changed = False
            if obj.line_color != line['hex_color']:
                obj.line_color = line['hex_color']
                is_changed = True
            if obj.line_name != line['name']:
                obj.line_name = line['name']
                is_changed = True
            if obj.position_in_line != station['order']:
                obj.position_in_line = station['order']
                is_changed = True
            if obj.station_name != station['name']:
                obj.station_name = station['name']
                is_changed = True
            if is_changed:
                changed += 1
            obj.save()
        else:
            MetroStation.objects.create(line_color=line['hex_color'], line_name=line['name'], position_in_line=station['order'], station_name=station['name'])
            created += 1

print(f"Objects created: {created}\nObjects changed: {changed}")
