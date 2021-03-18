def shop_list_size(request):
    user = request.user
    count = user.purchases.all().count() if user.is_authenticated else 0
    return {'shop_list_size': count}
