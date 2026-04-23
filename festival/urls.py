from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('palcos/', views.palcos_view, name='palcos'),
    path('concerto/<int:id>/', views.concerto_view, name='concerto'),
    path('dias/', views.dias_view, name='dias'),
]
