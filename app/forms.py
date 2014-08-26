# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import (MaxLengthValidator, MinLengthValidator, RegexValidator,
    MinValueValidator, MaxValueValidator, validate_email)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions

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

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            PrependedText('dni', '#'),
            'paterno',
            'materno',
            'nombre',
            PrependedText('edad', '#'),
            'direccion',
            PrependedText('email', '@'),
            PrependedText('fijo', '#'),
            PrependedText('movil', '#'),
            'universidad',
            'facultad',
            'carrera',
            'titulo',
            'cargo',
            'grado',
            'investigacion',
            FormActions(
                Submit('submit', u'Inscripción'),
                css_class='text-right'
            ),
        )

    class Meta:
        model = participante


class constancia_form(forms.Form):
    item = forms.CharField(label='ID ó DNI', max_length=8)
    item.validators.append(MinLengthValidator(1))
    item.validators.append(MaxLengthValidator(8))
    item.validators.append(RegexValidator(regex="^[0-9]+$"))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    helper.layout = Layout(
        PrependedText('item', '#'),
        FormActions(
            Submit('submit', u'Constancia'),
            css_class='text-right'
        ),
    )