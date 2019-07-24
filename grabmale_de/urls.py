# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('1/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<str:category_name>/', views.DetailView.as_view(), name='detail'),
    path('impressum/', views.ImpressumView.as_view(), name='impressum'),
]