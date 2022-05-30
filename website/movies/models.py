from django.db import models
from django.forms import CharField
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50,verbose_name='Filmin Adı')
    movie_type = models.CharField(max_length=60,verbose_name='Filmin türü')
    duration = models.CharField(max_length=50,verbose_name='Filmin süresi')
    description = models.TextField(max_length=350,verbose_name='Film açıklaması')
    image = models.CharField(max_length=100,verbose_name='Film kapağı')
    created_date = models.DateField(verbose_name='oluşturulma tarihi')
    Screening_date = models.CharField(max_length=20,verbose_name='Filmin Gösterime Giriş Tarihi')
    director = models.CharField(max_length=30,verbose_name='yönetmen')
    budget = models.CharField(max_length=20,verbose_name='Filmin bütçesi')
    revenues = models.CharField(max_length=20,verbose_name='Filmin Hasılatı')
    IsPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_image_path(self):
        return '/img/'+ self.image