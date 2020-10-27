from django.shortcuts import render
from django.core.mail import send_mail


def send_email(request):
    if request.method == 'POST':
        user_name = request.POST['contact_name']
        user_email = request.POST['contact_email']
        user_message = request.POST['contact_message']
        send_mail(
            "richiesta di contatto",
            f"{user_name} sended you this message: "
            f"{user_message} "
            f"from: {user_email}",
            'aciodo@hotmail.com',
            ['nicopelliz@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact_page.html', {'user_name': user_name})
    else:
        return render(request, 'contact_page.html', {})


