from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #index
    path('',views.accueil , name = "accueil"),
    path('laboHome',views.home , name = "home"),
    path('persoHome',views.persoHome , name = "persoHome"),
    path('patHome',views.patHome , name = "patHome"),
    path('add_Labo',views.add_Labo , name = "add_Labo"),
    path('add_Perso',views.add_Perso , name = "add_Perso"),
    path('add_Pat',views.add_Pat , name = "add_Pat"),
    path('labo/<str:labo_id>',views.labo , name = "labo"),
    path('perso/<str:perso_id>',views.perso , name = "perso"),
    path('pat/<str:pat_id>',views.pat , name = "pat"),
    path('edit_Labo',views.edit_Labo , name = "edit_Labo"),
    path('edit_Perso',views.edit_Perso , name = "edit_Perso"),
    path('edit_Pat',views.edit_Pat , name = "edit_Pat"),
    path('delete_Labo/<str:labo_id>',views.delete_Labo , name = "delete_Labo"),
    path('delete_Perso/<str:perso_id>',views.delete_Perso , name = "delete_Perso"),
    path('delete_Pat/<str:pat_id>',views.delete_Pat , name = "delete_Pat"),
]
