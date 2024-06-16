from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from forum.forms import ContactForm
from forum.services import EmailService


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'forum/contact_form.html'
    email_service = EmailService()

    def form_valid(self, form):
        try:
            self.email_service.send(
                form.cleaned_data.get('fullname'),
                form.cleaned_data.get('subject'),
                form.cleaned_data.get('email'),
                form.cleaned_data.get('message')
            )
        except Exception as e:
            messages.add_message(
                self.request,
                messages.WARNING,
                'Algo deu errado. Tente novamente mais tarde.'
            )
        else:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                'Mensagem enviada com sucesso!'
            )
        return super().form_valid(form)
