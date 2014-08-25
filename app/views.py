from django.shortcuts import render
from forms import participante_form

def home_view(request):
    form = participante_form()
    args = {}
    #args.update(csrf(request))
    args['form'] = form
    return render(request, 'home.html', args)
