'''import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from django.shortcuts import render


    def send_email(request):
        if request.method == 'POST':
            user_name = request.POST['contact_name']
            user_email = request.POST['contact_email']
            user_message = request.POST['contact_message']
        message = Mail(
            from_email=user_email,
            to_emails=['nicopelliz@gmail.com', 'aciodo@hotmail.com'],
            subject='Contact Request' + user_name,
            plain_text_content=user_message,
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

        return render(request, 'contact_page.html', {'user_name': user_name})
    else:
        return render(request, 'contact_page.html', {})'''

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


