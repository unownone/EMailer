from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.mail import EmailMessage
import datetime
from django.conf import settings


def sendMail(request):
    if request.method == 'GET':
        return render(request, 'mail.html')
    else:
        email = request.POST.get('email')
        if email=='':
            return HttpResponse('NOT WORKING')
        else:
            subject ='HI! AWESOME RIGHT?!'
            mail =f'''
                Hi! Hola From Imon!
                Welcome! You have received this email because you wanted this.
                The Time currently is : {datetime.datetime.now()}.
                Have Fun!
            '''
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = [email]
            msg = EmailMessage(subject,mail,to=to_mail).send()
        return HttpResponseRedirect('/')