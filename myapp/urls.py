from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index_templete, name='index_temp'),
    path('generate/', views.generate_index, name='generate_index'),
    path('pricing/', views.pricing_index, name='pricing_index'),
    path('history/', views.history_index, name='history_index'),
    path('../../gallery/', views.gallery_index, name='gallery_index'),
]
