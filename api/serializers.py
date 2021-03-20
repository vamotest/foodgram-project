from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from api.models import Favorite
from api.models import Purchase
from api.models import Subscription
from recipes.models import Ingredient


def validate_author(data):
    if data.get('author') == data.get('user'):
        raise ValidationError('Нельзя подписаться на самого себя')
    return data


class IngredientSerializer(ModelSerializer):
    class Meta:
        fields = ('title', 'dimension')
        model = Ingredient


class SubscriptionSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('author', 'user')
        model = Subscription
        validators = (validate_author, )


class FavoriteSerializer(ModelSerializer):
    class Meta:
        fields = ('recipe',)
        model = Favorite


class PurchaseSerializer(ModelSerializer):
    class Meta:
        fields = ('recipe',)
        model = Purchase
