from django.urls import path
from . import views

app_name = 'festival'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dias/', views.dias_view, name='dias'),
    path('dia/<int:dia_id>/', views.dia_view, name='dia'),
    path('palcos/', views.palcos_view, name='palcos'),
    path('concerto/<int:concerto_id>/', views.concerto_view, name='concerto'),
    path('edita/<int:concerto_id>/', views.edita_view, name='edita'),
    path('apaga/<int:concerto_id>/', views.apaga_view, name='apaga'),
]