from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
# # from django.core.mail import send_mail
# from tut2 import settings


def app1_view(request):
    # list_send = ['sagar.neupane419@gmail.com',]
    # email_from = settings.EMAIL_HOST_USER
    # subject_mail = "Lottery Ticket!!"
    # message_mail = "Dear Customer you have won $250 million in the lottery and for the confirmation please fill up " \
    #                "the kyc given in the link "
    # print(email_from)
    # send_mail(subject_mail, message_mail, email_from, list_send, fail_silently=True)
    return render(request, "app1.html")
