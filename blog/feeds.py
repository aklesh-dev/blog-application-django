from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

# --subclass the Feed class of the syndication framework
class LatestPostsFeed(Feed):
    title = 'My blog'
    # -- to generate the URL for the link attribute.
    link = reverse_lazy('blog:post_list_by_tag')
    description = 'New posts of my blog.'

    # -- items() methods retrieves the objects to be included in the feed
    # -- retreiving only five published posts for this feed.
    def items(self):
        return Post.published.all() [:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
    
    