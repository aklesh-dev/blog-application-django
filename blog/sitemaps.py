from django.contrib.sitemaps import Sitemap
from .models import Post

# -- changefreq and priority attributes indicate the change frequency of the post pages 
# -- and their relevance in the website(the maxmimum value is 1)
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    # -- returns the QuerySet of objects to include in this sitemap
    def items(self):
        return Post.published.all()
    
    # --lastmod method receives each object returned by items() and returns the last time the object was modified
    def lastmod(self, obj):
        return obj.update