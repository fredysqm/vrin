from django.shortcuts import render
from django.core.context_processors import csrf

from forms import participante_form, constancia_form


def home_view(request):
    return render(request, 'home.html')


def inscripcion_view(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = participante_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inscripcion_final.html')
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
            item = form.cleaned_data.get('item')
            if len(item) < 8:
                item = int(item)
            else:
                pass
            return render(request, 'constancia_print.html')
    else:
        form = constancia_form()
    args['form'] = form
    return render(request, 'constancia.html', args)


def constancia_print_view(request, id):
    return render(render, 'constancia_print.html', id)