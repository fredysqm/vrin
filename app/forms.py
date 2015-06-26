# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import (MaxLengthValidator, MinLengthValidator, RegexValidator,
    MinValueValidator, MaxValueValidator, validate_email)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button, Fieldset
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions

from .models import participante, asistencia, evento


class participante_crear_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(participante_crear_form, self).__init__(*args, **kwargs)
        self.fields["dni"].validators.append(MinLengthValidator(8))
        self.fields["dni"].validators.append(RegexValidator(regex="^[0-9]+$"))
        self.fields["edad"].validators.append(MinValueValidator(12))
        self.fields["edad"].validators.append(MaxValueValidator(128))
        self.fields["edad"].required=False
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
            Fieldset(u'<span class="glyphicon glyphicon-pencil"></span> Formato de Inscripción',
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
            ),
            FormActions(
                Submit('submit', u'Inscripción'),
                css_class='text-right'
            ),
        )

    class Meta:
        model = participante
        exclude = ()


class participante_constancia_form(forms.Form):
    dni = forms.CharField(label='DNI', max_length=8)
    dni.validators.append(MinLengthValidator(1))
    dni.validators.append(MaxLengthValidator(8))
    dni.validators.append(RegexValidator(regex="^[0-9]+$"))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    helper.layout = Layout(
        Fieldset(u'<span class="glyphicon glyphicon-pencil"></span> Reporte Constancia',
                PrependedText('dni', '#'),
        ),

        FormActions(
            Submit('submit', u'Constancia'),
            css_class='text-right'
        ),
    )

    def clean_dni(self):
        item = self.cleaned_data['dni']
        try:
            inscrito = participante.objects.get(dni=item)
        except:
            raise forms.ValidationError(u'DNI no esta registrado.')
        return item

class asistencia_form(forms.ModelForm):
    dni = forms.CharField(required=True, )

    def __init__(self, *args, **kwargs):
        super(asistencia_form, self).__init__(*args, **kwargs)
        self.fields['evento'].queryset = evento.objects.filter(cerrado=False)
        self.fields['dni'].widget.attrs['minlength'] = '8'
        self.fields['dni'].widget.attrs['maxlength'] = '8'
        self.fields['dni'].widget.attrs['autocomplete'] = 'off'
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            'evento',
            PrependedText('dni', '#'),
        )

    class Meta:
        model = asistencia
        exclude = ()