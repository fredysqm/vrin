from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from models import participante, evento, asistencia
from forms import participante_form, constancia_form, asistencia_form


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


@login_required(login_url='/admin')
def asistencia_view(request):
    args = {}
    args['form'] = asistencia_form()
    return render(request, 'asistencia.html', args)


@login_required(login_url='/admin')
def asistencia_registro_view(request, evento_id, participante_id):
    o_evento = get_object_or_404(evento,pk=evento_id)
    if not o_evento.cerrado:
        o_participante = get_object_or_404(participante,pk=participante_id)
        try:
            obj = asistencia()
            obj.evento = o_evento
            obj.participante = o_participante
            obj.save()
        except:
            return HttpResponse('duplicado')
        return HttpResponse('ok')
    else:
        return HttpResponse('evento cerrado')