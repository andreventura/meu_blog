from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)
    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'ventura11@gmail.com'
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Mensagem: %(mensagem)s
        """ % self.cleaned_data
        send_mail(subject=titulo,message=texto,from_email=destino,recipient_list=[destino],)

def contato(request):
    # form = FormContato() <== substituido pelo codigo abaixo
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            # raise Exception('oi')         
            form.enviar()
            mostrar = 'Contato enviado!'
        else:
            form = FormContato()

    return render_to_response('contato.html',locals(),context_instance=RequestContext(request),)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ventura11@gmail.com'
EMAIL_HOST_PASSWORD = '172349av'
EMAIL_SUBJECT_PREFIX = '[Blog do Alatazan]'
EMAIL_PORT = 587
