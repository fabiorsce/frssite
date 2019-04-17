from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views
from . import settings
from .sitemaps import StaticViewSitemap
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views


admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('home/', views.index),
    path('cgrtbilling/', views.cgrtbilling, name='cgrtbilling'),
    path('estatbio/', views.estatbio, name='estatbio'),
    path('admin/login/', auth_views.LoginView.as_view(), kwargs={"template_name":"admin/inv_login.html"}, name='login'),
    path('admin/', admin.site.urls),
    path('qa/', include('qa.urls')),
    path('mr/', include('mr.urls')),
    path('df/', include('df.urls')),
    path('loc/', include('loc.urls')),
    path('cron/', include('cron.urls')),
    path('sitemap\.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
