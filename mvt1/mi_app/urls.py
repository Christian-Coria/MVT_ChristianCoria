from django.contrib import admin
from django.urls import path
from mi_app.views import presentando,presentando_mascotas,presentandome,mostrando_index

urlpatterns = [
    path('mis_parientes', presentando),
    path('mis_mascotas', presentando_mascotas),
    path('mis_datos', presentandome),
    path('mi_pagina', mostrando_index),
]