from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from models import participante
from forms import participante_form, constancia_form


def inscripcion_view(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = participante_form(request.POST)
        if form.is_valid():
            form.save()
            args['inscrito'] = participante.objects.get(dni=form.cleaned_data.get('dni'))
            return render(request, 'inscripcion_final.html', args)
    else:
        form = participante_form()
    args['form'] = form
    return render(request, 'inscripcion.html', args)


def constancia_view(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = constancia_form(request.POST)
        if form.is_valid():
            item = form.cleaned_data.get('dni')
            return HttpResponseRedirect(
                reverse('constancia_print_url', args=[item])
                )
    else:
        form = constancia_form()
    args['form'] = form
    return render(request, 'constancia.html', args)


def constancia_print_view(request, id):
    args = {}
    inscrito = get_object_or_404(participante,dni=id)
    args['inscrito'] = inscrito
    return render(request, 'constancia_print.html', args)