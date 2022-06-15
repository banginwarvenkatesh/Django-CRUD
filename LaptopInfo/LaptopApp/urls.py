from django.urls import path
from . import views

urlpatterns = [
    path('lapform/', views.lapForm, name='lap_form'),
    path('laptable/', views.LapView, name='lap_table'),
    path('update/<int:id>/', views.updateLap, name='lap_update'),
    path('delete/<int:id>/', views.deleteLap, name='lap_delete')
]