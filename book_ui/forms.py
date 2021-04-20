#from django.forms import forms
from .models import DemoModel
from book_api.models import BookModel, PhrasesModel, PublisherModel, AuthorModel

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

class PublisherForm(ModelForm):
    class Meta:
        model = PublisherModel
        fields = ['name','descripton']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Publisher Name", "class": "form-control"}
        )
        self.fields["descripton"].widget.attrs.update(
            {"placeholder": "Description", "class": "form-control"}
        )



class AuthorForm(ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['first_name','last_name','author_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"placeholder": "First Name", "class": "form-control"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"placeholder": "Last Name", "class": "form-control"}
        )
        self.fields["author_image"].widget.attrs.update(
            {"placeholder": "Author Image"}
        )



class PhraseForm(ModelForm):
    class Meta:
        model = PhrasesModel
        fields = ['phrase','book','trigger','object','status']

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
        self.fields["object"].widget.attrs.update(
            {"placeholder": "3dObject", "class":"form-control","id":"customFile"}
        )
        self.fields["trigger"].widget.attrs.update(
            {"placeholder": "Trigger", "class":"custom-file-input", "id":"customFile"}
        )


class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['name','description','book_cover','author','publisher','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Full Name", "class": "form-control"}
        )
        self.fields["description"].widget.attrs.update(
            {"placeholder": "Description", "class": "form-control"}
        )
        self.fields["book_cover"].widget.attrs.update(
            {"placeholder": "Book Cover", "class": "form-control"}
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



