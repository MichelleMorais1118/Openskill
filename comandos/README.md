Iniciar projeto Django


python -m venv venv
venv/Script/Activate
pip install django
djago-admin startproject project . 
python manage.py startapp contact

python manage.py runserver

------------------------------------------------------

Configurar o git

git config -- global user.name ' '
git config -- global user.email ' '
git config -- global init.defaultBranch main
# configurar git ignore
git init
git add .
git commit -m ' '

# fecha git 
rm -r .git 


git remote add origin 
git branch -M main
git push -u origin main
--------------------------------------------------
migrando  base de dados do django

python manage.py makemigrations
python manage.py migrate

usuario e senha

python manage.py createsuperuser
python manage.py changepassword USERNAMe

python manage.py shell
from contact.models import Contact
Contact
c = Contact(nome = 'Hora Padel')
c
c.save()
c.telefone = '61998765432'
c.save()
c.delete()

c = contact.objects.get()
c
c.nome = padel
c = contact.objects.all()
for contato in c: nome
c = contact.objects.filter(id=10)
c
c = contact.objects.all().order_by('id')
c = contact.objects.create()