from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from www.models import LoanReq
from www.forms import LoanReqForm
from datetime import datetime


def index(request):
    if request.method == 'POST':
        form = LoanReqForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            aLoan = LoanReq(req_amount_ini=cd['req_amount_ini'],
              req_purpose=cd['req_purpose'],
              req_date=datetime.now())
            aLoan.save()
            return HttpResponseRedirect('print_redirect.html')
    else:
        form = LoanReqForm()
    return render(request, 'www/index.html', {'form': form})


def print_redirect(request):
    return render(request, 'www/print_redirect.html')
