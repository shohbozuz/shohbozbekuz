from django.contrib import admin
from django.urls import path

# intro o'z ichiga views ni olib keladi
from intro import views
from intro.views import index

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel manzili
    path('', index, name='index'),  # Bosh sahifa manzili (index view)
    path('icons/', views.icon_list, name='icon_list'),  # Ikonalarni ro'yxatini ko'rsatish manzili
    path('icons/new/', views.icon_create, name='icon_create'),
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/new/', views.skill_create, name='skill_create'),
    path('navbar/', views.navbar_link, name='navbar_link'),  # Navbar linklarni olish uchun URL
    path('me/', views.men_haqimda, name='men_haqimda'),
    path('konikmashu/', views.konikma_shu, name='konikma_shu'),

]

from django.conf import settings
from django.conf.urls.static import static

# Debug holatida media fayllarini serverdan olish
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
