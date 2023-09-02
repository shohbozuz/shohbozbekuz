from django import forms
from .models import Icon, Skill


class IconForm(forms.ModelForm):
    class Meta:
        model = Icon  # Modelimizni ko'rsatamiz
        fields = ['name', 'class_name', 'url']  # Formada ko'rsatiladigan maydonlar ro'yxati

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill  # Modelimizni ko'rsatamiz
        fields = ['skill_name', 'skill_image']  # Formada ko'rsatiladigan maydonlar ro'yxati


