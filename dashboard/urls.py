from django.urls import path
from .views import vista_inicio, vista_dashboard1, vista_dashboard2, vista_dashboard3, vista_dashboard4, actualizar_dashboard1, actualizar_dashboard2, actualizar_dashboard3, actualizar_dashboard4

urlpatterns = [
    path('', vista_inicio, name='inicio'),
    path('dashboard1/', vista_dashboard1, name='dashboard1'),
    path('dashboard2/', vista_dashboard2, name='dashboard2'),
    path('dashboard3/', vista_dashboard3, name='dashboard3'),
    path('dashboard4/', vista_dashboard4, name='dashboard4'),
    path('actualizar_dashboard1/', actualizar_dashboard1, name='actualizar_dashboard1'),
    path('actualizar_dashboard2/', actualizar_dashboard2, name='actualizar_dashboard2'),
    path('actualizar_dashboard3/', actualizar_dashboard3, name='actualizar_dashboard3'),
    path('actualizar_dashboard4/', actualizar_dashboard4, name='actualizar_dashboard4'),
]
