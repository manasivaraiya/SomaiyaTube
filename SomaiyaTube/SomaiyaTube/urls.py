from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from website import views

class HomePageView(TemplateView):
    template_name = 'home.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('',HomePageView.as_view(),name='home'),
    path('',views.homepage,name='homepage'),
    url(r'^view/(?P<pk>\d+)/$', views.video, name='ViewVideo'),
    path('upload/',views.upload,name="UploadVideo"),
    path('search_result/',views.SearchResultsView.as_view(),name="Search"),
    path('trending_results/',views.Trending_View.as_view(),name="trend"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
