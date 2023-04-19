from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    # 관리자 페이지에서 버거 정보 나타내기
    def __str__(self):
        return self.name