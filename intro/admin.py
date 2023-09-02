from django.contrib import admin
from .models import Intro, Icon, NavbarLink, About, Skill, konikmalar

admin.site.register(Intro)
admin.site.register(Icon)
admin.site.register(Skill)
admin.site.register(NavbarLink)  # NavbarLink modelini ham ro'yhatga qo'shing
admin.site.register(About)
admin.site.register(konikmalar)

