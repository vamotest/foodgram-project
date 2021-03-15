from django import template

register = template.Library()


@register.filter(name='parse_tags')
def parse_tags(get):
    return get.getlist('tag')


@register.filter(name='set_tag_qs')
def set_tag_qs(request, tag):
    new_req = request.GET.copy()
    tags = new_req.getlist('tag')
    
    if tag.title in tags:
        tags.remove(tag.title)
    else:
        tags.append(tag.title)
    
    new_req.setlist('tag', tags)
    return new_req.urlencode()
