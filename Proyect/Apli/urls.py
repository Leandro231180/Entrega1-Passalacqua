from django.urls import path
from Apli import views
from django.conf.urls.static import static

urlpatterns=[

    path('', views.inicio),
    path('buscarFamilia/', views.busqueda_quenobusca, name='buscar'),
    path('familia', views.familia, name='familia'),
    path('placas', views.placas, name='placas' ),
    path('videojuegos',views.videojuegos, name='videojuegos'),
    path('buscar/', views.buscar),

]