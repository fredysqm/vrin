from django.shortcuts import render
from django.core.context_processors import csrf

from forms import participante_form


def home_view(request):
    return render(request, 'home.html')

def inscripcion_view(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = participante_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inscripcion_url'))
    else:
        form = participante_form()

    args['form'] = form
    return render(request, 'inscripcion.html', args)

def constancia_view(request):
    return render(request, 'constancia.html')