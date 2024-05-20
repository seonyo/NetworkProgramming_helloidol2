from django.urls import path

from . import views

app_name = "콩순이"

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]