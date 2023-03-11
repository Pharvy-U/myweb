from django.forms import ModelForm, Textarea, CheckboxSelectMultiple
from .models import Message, Project, Blog


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 10})
            # 'category': CheckboxSelectMultiple(),
        }


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'tags': CheckboxSelectMultiple()
        }
