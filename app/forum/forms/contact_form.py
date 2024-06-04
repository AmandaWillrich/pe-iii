from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(label='Nome Completo')
    subject = forms.CharField(max_length=100, label='Assunto')
    message = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(
            attrs={'name':'message'}
        )
    )
