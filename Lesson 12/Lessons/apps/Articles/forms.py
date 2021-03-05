from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    text = forms.CharField(label='Текст', widget=forms.Textarea)