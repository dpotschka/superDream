from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        #return ['index']
        return ['books', 'artForSale', 'guitarVideos']

    def location(self, item):
        return reverse(item)

# changefreq can be 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'