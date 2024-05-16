from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # 데이터를 처음 넣을 때 자동으로 넣겠냐
    updated_at = models.DateTimeField(auto_now=True)
