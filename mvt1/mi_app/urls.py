from django.contrib import admin
from django.urls import path
from mi_app.views import presentando,presentando_mascotas,presentandome

urlpatterns = [
    path('mis_parientes', presentando),
    path('mis_mascotas', presentando_mascotas),
    path('mis_datos', presentandome)
]