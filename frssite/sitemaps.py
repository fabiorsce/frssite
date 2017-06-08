from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return ['food_request', 'food_request_kitchen_view', 'food_request_cashier_view', 'get_location', 'random_test', 'employee-list']

    def location(self, item):
        return reverse(item)