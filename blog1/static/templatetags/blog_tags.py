from django import template
from  blog1.models import Post,Category
register = template.Library()

@register.simple_tag
def get_recent_posts():
    '''按照时间排序筛选所有文章并选择前五篇文章'''
    return Post.objects.all().order_by('-created_time')


@register.simple_tag
def archives():
    '''按照年月筛选出文章'''
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    '''按照分类筛选出文章'''

    return Category.objects.all()