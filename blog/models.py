from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    foto = models.FileField(upload_to="image_users/", null=True, blank=True, default="image_users/default.png")

    def __str__(self):
        return self.nome

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mensage = models.TextField()
    data_publicacao = models.DateField()