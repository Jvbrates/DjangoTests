from django.shortcuts import render

# Create your views here.
from .forms import sendMail



def sendMailView(request):
    if not request.session.get('credentials', False):
        pass
    if request.method == 'POST':
        form = sendMail(request.POST)

    form = sendMail()

    return render(request, "sendmail/send.html", {"form": form})