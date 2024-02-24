from django.urls import path
from . import views
app_name = 'mantenimiento'
urlpatterns = [
    path('ordenesdetrabajo/', views.listarOrdenesDeTrabajoView.as_view(), name='ordenesdetrabajo'),
    path('add/', views.AddOrdendeTrabajoCreateView.as_view(), name='add_ordendetrabajo_view'),
    path('update/<pk>/', views.ActualizarTicketPUCView.as_view(), name='update_ordendetrabajo_view'),
    path('delete/<pk>/', views.EliminarOrdenDeTrabajoView.as_view(), name='delete_ordendetrabajo_view'),
]