from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from forum.forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'forum/contact_form.html'


    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Enviado com sucesso!'
        )
        return super().form_valid(form)
