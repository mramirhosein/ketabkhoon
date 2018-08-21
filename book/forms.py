import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_data = forms.DateField(help_text='Enter a date between now and four weeks.')

    def clean_renewal_data(self):
        data = self.cleaned_data['renewal_data']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal is past.'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal mor than 4 weeks ahead.'))

        return data