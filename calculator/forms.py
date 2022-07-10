from django.forms import ModelForm
from django.forms.models import (inlineformset_factory, modelformset_factory, modelform_factory)
from .models import Quote, QuoteItem
from django import forms


class QuoteForm(ModelForm):

    class Meta:
        model = Quote
        fields = ["customer", "user_id", "comment"]
        exclude=["user_id"]


class QuoteItemForm(ModelForm):

    class Meta:
        model = QuoteItem
        fields = ["name", "quantity"]
