from django.contrib import admin
from django.urls import path, include
from app.views import home
from app.views import about
from app.views import service
from app.views import contact
from app.views import schedule
from app.views import convenios, categorias_convenios
from app.views import anuncios, categorias_anuncios
from app.views import equip_hosp
from app.views import eventos
from app.views import ficha_filiacao
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', about),
    path('diretoria/', diretoria),
    path('locacoes/', service),
    path('contato/', contact),
    path('agenda/', schedule),
    path('convenios/', convenios),
    path('convenios<pk>/', categorias_convenios),
    path('anuncios/', anuncios),
    path('anuncios/<pk>/', categorias_anuncios),
    path('equipamentos/', equip_hosp),
    path('filiacao/formulario/', ficha_filiacao),
    path('filiacao/', filiacao),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('eventos/', eventos),
    path('photologue/', include('photologue.urls', namespace='photologue')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
