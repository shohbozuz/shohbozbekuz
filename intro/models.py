from django.db import models


# Intro modeli: Bosh sahifadagi ma'lumotlar uchun
class Intro(models.Model):
    logo_text = models.CharField(max_length=50, default='Shohbozbek')  # Logo matni
    logo_logo = models.CharField(max_length=50, default='fab fa-dev')  # Logo Logo
    rezume_text = models.CharField(max_length=50, default='Default Resume Text')  # Rezume tugmasi matni
    file = models.FileField(upload_to='resumes/', default='default_resume.pdf')  # Faylni yuklash uchun maydon
    image = models.ImageField(upload_to='images/')  # Rasm maydoni
    title = models.CharField(max_length=100)  # Sahifa sarlavhasi
    content = models.TextField()  # Sahifa matni

    def __str__(self):
        return self.title  # Intro obyekti nomini qaytaradi


class NavbarLink(models.Model):
    home = models.CharField(max_length=50, default='Home')
    about = models.CharField(max_length=50, default='About')
    skills = models.CharField(max_length=50, default='Skills')
    education = models.CharField(max_length=50, default='Education')
    work = models.CharField(max_length=50, default='Work')
    experience = models.CharField(max_length=50, default='Experience')
    contact = models.CharField(max_length=50, default='Contact')

    def __str__(self):
        return self.home


class About(models.Model):
    men_haqimda = models.CharField(max_length=50, default='Men haqimda')
    mening_ismim = models.CharField(max_length=50, default="Shohbozbek Turg'unov")
    kasbim = models.CharField(max_length=50, default='Full Stack Developer')
    men_haqimda_description = models.TextField()
    mening_rasmim = models.ImageField(upload_to='images/', )  # Standart rasm

    def __str__(self):
        return self.men_haqimda


# Icon modeli: Ikonalarni saqlash uchun
class Icon(models.Model):
    name = models.CharField(max_length=50)  # Ikonaning nomi
    class_name = models.CharField(max_length=50)  # Font Awesome klass nomi
    url = models.URLField()  # Ikonaga havola

    def __str__(self):
        return self.name  # Icon obyekti nomini qaytaradi

class konikmalar(models.Model):
    konikma_shunchaki = models.CharField(max_length=50)

    def __str__(self):
        return self.konikma_shunchaki

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_image = models.ImageField(upload_to='images/skills/')

    def __str__(self):
        return self.skill_name
