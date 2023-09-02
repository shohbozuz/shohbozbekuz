from django.shortcuts import render
from .models import Intro, Icon, NavbarLink, About, Skill, konikmalar


# Bosh sahifa - index view
def index(request):
    intro = Intro.objects.first()
    icons = Icon.objects.all()
    skills = Skill.objects.all()
    navbar_links = NavbarLink.objects.first()  # NavbarLink obyektini olish
    me = About.objects.first()
    konikma_me = konikmalar.objects.first()
    context = {
        'intro': intro,
        'icons': icons,
        'skills': skills,
        'navbar': navbar_links,  # navbar ni contextga qo'shish
        'about': me,
        'konikma_me': konikma_me,
    }
    return render(request, 'base.html', context)



def navbar_link(request):
    navbar_links = NavbarLink.objects.first()
    context = {
        'navbar': navbar_links,
    }
    return render(request, 'base.html', context)


def men_haqimda(request):
    me = About.objects.first()
    context = {
        'malumot': me,
    }
    return render(request, 'base.html', context)

def konikma_shu(request):
    konikma_me = About.objects.first()
    context = {
        'konikma_me': konikma_me,
    }
    return render(request, 'base.html', context)




# Ikonalarni ro'yxatini ko'rsatish - icon_list view
def icon_list(request):
    icons = Icon.objects.all()  # Barcha ikonalarni olish
    context = {
        'icons': icons,  # Iconlar ro'yxatini contextga qo'shish
    }
    return render(request, 'base.html', context)  # Bosh sahifani ko'rsatish


# Yangi ikon yaratish - icon_create view
def icon_create(request):
    # Yangi ikon yaratish uchun
    pass


def skill_list(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'base.html', context)


def skill_create(request):
    pass


