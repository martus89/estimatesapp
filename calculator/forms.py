from django.forms import ModelForm
from django.forms.models import (inlineformset_factory, modelformset_factory, modelform_factory)
from .models import *
from django import forms


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["customer", "comment"]


class QuoteItemForm(forms.ModelForm):
    class Meta:
        model = QuoteItem
        fields = "__all__"


QuoteItemFormSet = inlineformset_factory(
    Quote,
    QuoteItem,
    QuoteItemForm,
    can_delete=False,
    min_num=1,
    extra=0,
    can_delete_extra=True

)
