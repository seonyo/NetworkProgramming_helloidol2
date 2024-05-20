from django.shortcuts import render
from django.views.generic import ListView

from .models import Character


# Create your views here.
class CharacterListView(ListView):
    model = Character
    # character_list = Character.objects.all()  #DB에 모델 데이터 다 가져오자
    # return render(request, '콩순이/character_list.html', context = {'character_list' :
    # charcater_list})      #모델_list.html이 모델_list라는 키로 DB에서 가져온 데이터 넣어서 render 하자
