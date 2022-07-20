from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# --This variable is an instance of template.Library & used to register template tags and filter
register = template.Library()

# --simple template tag. it return string
@register.simple_tag
def total_post():
    return Post.published.count()

# --inclusion tag. it return template
@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {'latest_posts':latest_posts}

# --simple template tag that display most commented posts.
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# --custom template filter
@register.filter(name='markdown')
def markdown_formate(text):
    return mark_safe(markdown.markdown(text))