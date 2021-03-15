def shop_list_size(request):
    if not request.user.is_authenticated:
        return {'shop_list_size': 0}
    return {'shop_list_size': request.user.purchases.all().count()}
