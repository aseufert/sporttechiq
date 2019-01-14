from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, HttpResponse
from showcase.models import Station, FieldLayout
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        print('request get')
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            mail_msg = "Contact page message sent by {}\n\n{}".format(from_email, message)

            try:
                send_mail(
                    subject,
                    mail_msg,
                    'noreply@sporttechiq.com',
                    ['amseufert@gmail.com', 'brian.moure1@gmail.com']
                )

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/')

    return render(request, "contact.html", {'form': form})


def index(request):
    if request.user.groups.exists():
        group = str(request.user.groups.all()[0])
        return render(request, 'index.html', context={'group': group})
    else:
        return render(request, 'index.html')


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def format(request):
    stations = Station.objects.all().order_by('index')
    field_layouts = FieldLayout.objects.all()

    return render(request, 'format.html', context={
        'stations': stations,
        'field_layouts': field_layouts,
    })
