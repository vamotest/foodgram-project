from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'cooking_time', 'text', 'image')
        widgets = {'tags': forms.CheckboxSelectMultiple()}
