from django.shortcuts import render


def page_bad_request(request, exception):
    return render(request, 'misc/404.html', status=404)


def page_not_found(request, exception):
    return render(request, 'misc/404.html', status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
