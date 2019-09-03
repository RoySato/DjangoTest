from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'
urlpatterns = [
    #path('post', views.PostView, name='post'),
    path('create',  views.PostCreateView.as_view(), name='create'),
    path('created', views.created, name='created'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
