from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import FormFiliacao
from .models import *

def ficha_filiacao(request):
    formFiliacao = FormFiliacao(request.POST or None)
    context = {'formFiliacao': formFiliacao}
    if request.method == 'POST':
        if form.is_valid():
            formFiliacao.save()
            return redirect('/')
    else:
        return render(request, "formFiliacao.html", context)


def equip_hosp(request):
    equip_hosp = PostEquipHosp.objects.all()
    if request.method == 'POST':
        if PostEquipHosp.is_valid():
            PostEquipHosp.save()
            return redirect('equipamentos/')

    return render(request, "equipamentos.html", {'equip_hosp': equip_hosp})


def categorias_anuncios(request, pk):
    categorias = CategoriaAnuncio.objects.get(id=pk)
    anuncio = PostAnuncio.objects.all()
    categoria_1 = PostAnuncio.objects.filter(categoria__id=1)
    categoria_2 = PostAnuncio.objects.filter(categoria__id=2)
    categoria_3 = PostAnuncio.objects.filter(categoria__id=3)
    categoria_4 = PostAnuncio.objects.filter(categoria__id=4)
    categoria_5 = PostAnuncio.objects.filter(categoria__id=5)
    categoria_6 = PostAnuncio.objects.filter(categoria__id=6)
    categoria_7 = PostAnuncio.objects.filter(categoria__id=7)
    categoria_8 = PostAnuncio.objects.filter(categoria__id=8)
    context = {'cat_1': categoria_1, 'cat_5': categoria_5,
                   'cat_2': categoria_2, 'cat_6': categoria_6,
                   'cat_3': categoria_3, 'cat_7': categoria_7,
                   'cat_4': categoria_4, 'cat_8': categoria_8,
               'categorias_anuncios': categorias, 'anuncio': anuncio}

    return render(request, "anuncios.html", context)


def anuncios(request):
    anuncios = PostAnuncio.objects.all()
    if request.method == 'POST':
        if PostAnuncio.is_valid():
            PostAnuncio.save()
            return redirect('anuncios/')

    return render(request, 'anuncios_principal.html', {'anuncios': anuncios})


def categorias_convenios(request):
    convenios = PostConvenio.objects.all()
    if request.method == 'POST':
        if PostAnuncio.is_valid():
            PostConvenio.save()
            return redirect('convenios/')

    return render(request, 'convenios_geral.html', {'convenios': convenios})


def home(request):
    return render(request, "home.html")


def convenios(request):
    conveniosPost = PostConvenio(request.POST or None)
    context = {'conveniosPost': conveniosPost}
    if request.method == 'POST':
        if conveniosPost.is_valid():
            conveniosPost.save()
            return redirect('eventos/')
    else:
        return render(request, "blog_eventos.html", context)
    return render(request, "convenios.html")

def eventos(request):
    eventos = PostEvento.objects.all()
    eventosPost = PostEvento(request.POST or None)
    if request.method == 'POST':
        if eventosPost.is_valid():
            eventosPost.save()
            return redirect('')

    return render(request, "blog_eventos.html", {'eventos': eventos})


def about(request):
    return render(request, "sobre.html")


def contact(request):
    return render(request, "contato.html")


def service(request):
    return render(request, "locacoes.html")


def schedule(request):
    return render(request, "agenda.html")


def diretoria(request):
    return render(request, "diretoria.html")

def filiacao(request):
    return render(request, "filiacao.html")