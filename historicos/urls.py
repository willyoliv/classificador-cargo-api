from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='historicos'

urlpatterns = [
    path('predict/', views.HistoricoPredict.as_view(), name='predict'),
]

urlpatterns = format_suffix_patterns(urlpatterns)