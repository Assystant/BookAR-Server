#from django.forms import forms
from .models import DemoModel
from book_api.models import BookModel, PhrasesModel

from django.forms import ModelForm




from django.db import models
from model_utils.models import TimeStampedModel




class Demoform(ModelForm):
    class Meta:
        model = DemoModel
        fields = ['name','phone']

#from django.forms import forms
# from appserver.book_api.models import BookModel
# from django.forms import ModelForm
#
class PhraseForm(ModelForm):
    class Meta:
        model = PhrasesModel
        fields = ['phrase','book','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phrase"].widget.attrs.update(
            {"placeholder": "Phrase", "class": "form-control"}
        )
        self.fields["status"].widget.attrs.update(
            {"placeholder": "Status", "class": "form-control"}
        )
        self.fields["book"].widget.attrs.update(
            {"placeholder": "Book", "class": "form-control"}
        )


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['name','description','author','publisher','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Full Name", "class": "form-control"}
        )
        self.fields["description"].widget.attrs.update(
            {"placeholder": "Description", "class": "form-control"}
        )
        self.fields["author"].widget.attrs.update(
            {"placeholder": "Author", "class": "form-control"}
        )
        self.fields["publisher"].widget.attrs.update(
            {"placeholder": "Publisher", "class": "form-control"}
        )
        self.fields["status"].widget.attrs.update(
            {"placeholder": "Status", "class": "form-control"}
        )



