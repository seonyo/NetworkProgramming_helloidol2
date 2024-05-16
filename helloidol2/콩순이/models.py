from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터를 처음 넣을 때 자동으로 넣겠냐
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'이름: {self.name}, 특징: {self.feature}, 만든 날짜: ${self.created_at}, 수정한 날짜 ${self.updated_at}'
