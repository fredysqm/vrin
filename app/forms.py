# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import (MaxLengthValidator, MinLengthValidator, RegexValidator,
    MinValueValidator, MaxValueValidator, validate_email)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from models import participante


class participante_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(participante_form, self).__init__(*args, **kwargs)
        self.fields["dni"].validators.append(MinLengthValidator(8))
        self.fields["dni"].validators.append(RegexValidator(regex="^[0-9]+$"))
        self.fields["edad"].validators.append(MinValueValidator(8))
        self.fields["edad"].validators.append(MaxValueValidator(128))
        self.fields["email"].validators.append(validate_email)
        self.fields["fijo"].validators.append(RegexValidator(regex="^[0-9]+$"))
        self.fields["fijo"].required=False
        self.fields["movil"].validators.append(RegexValidator(regex="^[0-9]+$"))
        self.fields["movil"].required=False
        self.fields["titulo"].required=False
        self.fields["investigacion"].required=False

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    helper.add_input(Submit('submit', 'Inscripción', css_class='btn-primary'))

    class Meta:
        model = participante