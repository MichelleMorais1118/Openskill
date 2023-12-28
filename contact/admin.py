from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('id','nome','telefone')
    ordering = '-id',
   #list_filter = ('data_criada',)
    search_fields = 'id','nome',
    list_per_page = 5
    list_max_show_all= 100
    #list_editable = 'nome', 'telefone',
    list_display_links = 'id','nome',
    
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'nome',

    
@admin.register(models.Jogadore)
class JogadoreAdmin(admin.ModelAdmin):
    list_display = ('id','nome','apelido')
    ordering = '-id',
    search_fields = 'id','apelido',
    list_per_page = 5
    list_max_show_all= 100
    list_display_links = 'id','apelido',
    
@admin.register(models.Quadra)
class QuadraAdmin(admin.ModelAdmin):
    list_display = ('id','numero')
    ordering = '-id',
    list_per_page = 5
    list_max_show_all= 100
    search_fields = 'id','numero',
    
@admin.register(models.Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('id','numero')
    ordering = '-id',
    search_fields = 'id','numero',
    list_per_page = 5
    list_max_show_all= 100
    list_display_links = 'id','numero',