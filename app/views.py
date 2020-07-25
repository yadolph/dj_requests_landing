from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()

def index(request):
    came_from = request.GET.get('from-landing')
    if came_from == 'original':
        counter_click['original'] += 1
    elif came_from == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    land_style = request.GET.get('ab-test-arg')
    if land_style == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif land_style == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')


def stats(request):
    try:
        test_ratio = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        test_ratio = 'Мало данных'
    try:
        original_ratio = counter_click['original'] / counter_show['original']
    except ZeroDivisionError:
        original_ratio = 'Мало данных'
    return render_to_response('stats.html', context={
        'test_conversion': test_ratio,
        'original_conversion': original_ratio,
    })
