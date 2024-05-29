from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from users.forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = 'login'

    def form_valid(self, form, *args):
        form.save()
        messages.success(
            self.request,
            f'Bem-vindo (a), {form.cleaned_data.get('username')}!'
        )
        return redirect('login')
