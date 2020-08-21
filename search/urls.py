from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('keyword/', views.keyword, name='keyword'),
    path('video/', views.video, name='video'),
    path('theme/', views.theme, name='theme'),
    path('fifth/', views.fifth, name='fifth'),
    path('chart/', views.chart, name='chart'),
]