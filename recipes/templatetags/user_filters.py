from django import template
from django.contrib.auth import get_user_model

from api.models import Subscription

register = template.Library()
User = get_user_model()


@register.filter
def get_full_name_or_username(user):
    return user.get_full_name() or user.username


@register.filter
def is_subscribed_to(user, author):
    return Subscription.objects.filter(user=user, author=author).exists()
