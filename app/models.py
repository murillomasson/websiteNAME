from ckeditor.fields import RichTextField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

image = models.ForeignKey(
    'photologue.Photo',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    )

class CategoriaConvenio(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    descricao = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.descricao


class CategoriaAnuncio(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    descricao = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.descricao


class PostEvento(models.Model):
    titulo = models.CharField(
        max_length=100,
        unique=True
    )
    corpo = RichTextUploadingField(
    )
    imagem_previa = models.ForeignKey(
        'photologue.Photo',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Imagem prévia",
    )
    galeria = models.ForeignKey(
        'photologue.Gallery',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.titulo

    def publish(self):
        self.save()


class PostAnuncio(models.Model):
    id_anuncio = models.IntegerField(primary_key=True)
    data = models.DateTimeField(
        auto_now_add=True
    )
    titulo = models.CharField(
        max_length=50
    )
    telefone = models.CharField(
        max_length=12,
        null=True,
    )
    email = models.EmailField(
        null=True
    )
    texto_anuncio = models.TextField(
        max_length=500
    )
    categoria = models.ForeignKey(
        CategoriaAnuncio,
        on_delete=models.CASCADE
    )
    imagem_previa = models.ForeignKey(
        'photologue.Photo',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Imagem prévia",
    )
    galeria = models.ForeignKey(
        'photologue.Gallery',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.titulo


class PostEquipHosp(models.Model):
    AV_CHOICES = (
        ("Disponível", "Disponível"),
        ("Indisponível", "Indisponível"),
    )
    nome = models.CharField(
        max_length=200
    )
    foto = models.ImageField(
        upload_to="media/equip/",
        blank=True,
        null=True
    )
    quantidade = models.PositiveSmallIntegerField(
        help_text='Quantidade disponível'
    )
    disponibilidade = models.CharField(
        max_length=12,
        choices=AV_CHOICES,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nome
 # definir nome para default, fazer migracao, html statment if... for... looping das fotos em carrossel com for

class PostConvenio(models.Model):
    empresa = models.CharField(
        max_length=100
    )
    contato = models.TextField(
        max_length=100
    )
    texto_convenio = RichTextUploadingField()
    categoria = models.ForeignKey(
        CategoriaConvenio,
        on_delete=models.CASCADE,
        verbose_name='Categoria do Anúncio'
    )
    imagem_previa = models.ForeignKey(
        'photologue.Photo',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Imagem prévia",
    )
    galeria = models.ForeignKey(
        'photologue.Gallery',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
       return self.empresa
