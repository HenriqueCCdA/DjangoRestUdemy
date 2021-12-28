from django.urls import path
from django.urls import path

from cursos.views import CursoAPIView, AvalicaoAPIView


urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvalicaoAPIView.as_view(), name='avaliacao'),
]
