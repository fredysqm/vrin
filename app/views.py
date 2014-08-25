from django.shortcuts import render
from django.core.context_processors import csrf

from forms import participante_form

def home_view(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = participante_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_url'))
    else:
        form = participante_form()

    args['form'] = form
    return render(request, 'home.html', args)

def constancia_view(request, id):
    pass
