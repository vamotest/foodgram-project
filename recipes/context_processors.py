def shop_list_size(request):
    return {'shop_list_size': request.user.purchases.all().count()}
