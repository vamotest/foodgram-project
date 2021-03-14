from django.conf import settings
from django.core.paginator import Paginator


def get_paginated_view(request, some_list):
    paginator = Paginator(some_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator


def request_tags(request):
    return request.GET.getlist('tag', ('breakfast', 'lunch', 'dinner'))

