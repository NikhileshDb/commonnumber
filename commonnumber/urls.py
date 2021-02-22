
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('api/', views.apiOverview, name='api'),
    path('api/result-list/', views.ResultList,name='result-list'),
    path('api/result-detail/<str:pk>', views.ResultDetail,name='result-detail'),

]