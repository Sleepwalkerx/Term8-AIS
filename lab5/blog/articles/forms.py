from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Название статьи",
                    "class": "form-input",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Текст статьи",
                    "class": "form-textarea",
                    "rows": 10,
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if Article.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("Статья с таким названием уже существует.")

        return title