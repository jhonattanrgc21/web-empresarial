from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.
def contact(request):
    contact_form = ContactForms()
    if request.method == 'POST':
        contact_form = ContactForms(data = request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto', # Asunto
                'De {} {}\n\nEscribio\n\n{}'.format(name, email, content), # Cuerpo
                'no-contestar@imbox.mailtrap.io', # Origen
                ['django@jhonattanrgc21.net'], # Destino
                reply_to = [email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                return redirect(reverse('contact') + '?fail')
    return render(request, 'contact/contact.html', {'form': contact_form})