from django.shortcuts import render_to_response, redirect
import csv
from django.core.paginator import Paginator
from django.urls import reverse
from .settings import BUS_STATION_CSV
from urllib.parse import urlencode

stations = []
with open(BUS_STATION_CSV, newline='',  encoding='cp1251') as csvf:
    data = csv.DictReader(csvf)
    for row in data:
        stations.append({
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District']
        })

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = request.GET.get('page')
    if page == None:
        page = '1'
    paginator = Paginator(station_list, 20)
    counter = paginator.page(page)

    return render_to_response('index.html', context={
        'bus_stations': counter.object_list,
        'current_page': page,
        'prev_page_url': ('?'.join([reverse(bus_stations), urlencode(
            {'page': counter.previous_page_number()})])) if counter.has_previous() else False,
        'next_page_url': ('?'.join([reverse(bus_stations), urlencode(
            {'page': counter.next_page_number()})])) if counter.has_next() else False,
    })