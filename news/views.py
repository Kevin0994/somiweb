from django.shortcuts import render


from .models import Noticia, Comentario
# Create your views here.


def viewHomePage(request):
    noticias = Noticia.objects.all()
    return render(request, './home_page.html', {'noticias': noticias})

