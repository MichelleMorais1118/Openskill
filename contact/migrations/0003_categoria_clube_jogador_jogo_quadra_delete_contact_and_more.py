# Generated by Django 4.2.7 on 2023-11-20 16:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_foto_contact_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('data_criada', models.DateField(default=django.utils.timezone.now)),
                ('descricao', models.TextField(blank=True)),
                ('show', models.BooleanField(default=True)),
                ('funcionamento', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='pictures/%Y/%m/')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('data_criada', models.DateField(default=django.utils.timezone.now)),
                ('show', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, upload_to='pictures/%Y/%m/')),
                ('descricao', models.TextField(blank=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('data_criada', models.DateField(default=django.utils.timezone.now)),
                ('show', models.BooleanField(default=True)),
                ('placar', models.TextField(blank=True)),
                ('descricao', models.TextField(blank=True)),
                ('jogador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.jogador')),
            ],
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('funcionamento', models.CharField(max_length=100)),
                ('data_criada', models.DateField(default=django.utils.timezone.now)),
                ('show', models.BooleanField(default=True)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='jogo',
            name='quadra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.quadra'),
        ),
        migrations.AddField(
            model_name='clube',
            name='jogador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.jogador'),
        ),
        migrations.AddField(
            model_name='clube',
            name='quadra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.quadra'),
        ),
    ]
