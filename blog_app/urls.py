from django.urls import path
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.lists.as_view(),name='list'),
    path('detail/<slug:slug>/',views.detail.as_view(),name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)