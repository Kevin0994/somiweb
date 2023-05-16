from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_field = models.ImageField(upload_to='media', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.titulo
    

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self) :
        return self.contenido