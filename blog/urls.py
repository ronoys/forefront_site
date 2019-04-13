from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.home,name='blog-home'),
    url(r'^about/$', views.about,name='blog-about'),


]
