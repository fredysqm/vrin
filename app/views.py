from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView

from models import participante, evento, asistencia
from forms import participante_crear_form, participante_constancia_form


class participante_crear_view(CreateView):
    form_class = participante_crear_form
    template_name = 'participante/crear.html'
    def get_success_url(self): return reverse('participante_crear_final_url', args=(self.object.dni,))

class participante_crear_final_view(DetailView):
    model = participante
    template_name = 'participante/crear_final.html'

class participante_constancia_view(FormView):
    form_class = participante_constancia_form
    template_name = 'participante/constancia.html'
    def get_success_url(self):
        form = self.get_form()
        print form.cleaned_data.get('dni')
        return reverse('participante_constancia_print_url', args=(form.cleaned_data.get('dni'),))

class participante_constancia_print_view(DetailView):
    model = participante
    template_name = 'participante/constancia_print.html'




# def constancia_view(request):
#     args = {}
#     args.update(csrf(request))
#     if request.method == 'POST':
#         form = constancia_form(request.POST)
#         if form.is_valid():
#             item = form.cleaned_data.get('dni')
#             return HttpResponseRedirect(
#                 reverse('constancia_print_url', args=[item])
#                 )
#     else:
#         form = constancia_form()
#     args['form'] = form
#     return render(request, 'constancia.html', args)


# def constancia_print_view(request, id):
#     args = {}
#     inscrito = get_object_or_404(participante,dni=id)
#     args['inscrito'] = inscrito
#     return render(request, 'constancia_print.html', args)


# @login_required(login_url='/admin/')
# def asistencia_view(request):
#     args = {}
#     args['form'] = asistencia_form()
#     return render(request, 'asistencia.html', args)


# @login_required(login_url='/admin/')
# def asistencia_registro_view(request, evento_id, participante_id):
#     o_evento = get_object_or_404(evento,pk=evento_id)
#     if not o_evento.cerrado:
#         o_participante = get_object_or_404(participante,pk=participante_id)
#         try:
#             obj = asistencia()
#             obj.evento = o_evento
#             obj.participante = o_participante
#             obj.save()
#         except:
#             return HttpResponse('Registrado: ' + str(o_participante) + '<br>')
#         return HttpResponse('Registrado: ' + str(o_participante) + '<br>')
#     else:
#         return HttpResponse(u'Evento cerrado!' + '<br>')