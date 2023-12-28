from django.db import models
from django.utils import timezone
# Create your models here.
# idclube (primary key)
# nome (string), telefone (string),jogador (foreign key), quadra (foreign key), data_criada (date), descricao (text)
# categoria(foreign key), show (boolean), dono (foreign key)
# funcionamento (date), endereco (string), cep (integer)
# foto(imagem)


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
class Jogadore(models.Model):
    class Meta:
        verbose_name ='Jogador'
        verbose_name_plural ='Jogadores'
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    data_criada = models.DateField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    show = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    descricao = models.TextField(blank=True)
    
class Quadra(models.Model):
    numero = models.CharField(max_length=100)
    funcionamento = models.CharField(max_length=100)
    data_criada = models.DateField(default=timezone.now)
    show = models.BooleanField(default=True)
    descricao = models.TextField(blank=True)
    
class Jogo(models.Model):
    numero = models.CharField(max_length=100)
    quadra = models.ForeignKey(Quadra, on_delete=models.SET_NULL, blank=True, null=True)
    jogador = models.ForeignKey(Jogadore, on_delete=models.SET_NULL, blank=True, null=True)
    data_criada = models.DateField(default=timezone.now)
    show = models.BooleanField(default=True)
    placar = models.TextField(blank=True)
    descricao = models.TextField(blank=True)

class Clube(models.Model):
    cep = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    jogador = models.ForeignKey(Jogadore, on_delete=models.SET_NULL, blank=True, null=True)
    quadra = models.ForeignKey(Quadra, on_delete=models.SET_NULL, blank=True, null=True)
    data_criada = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    show = models.BooleanField(default=True)
    funcionamento = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    
    def __str__(self) -> str:
        return self.nome
    
    
