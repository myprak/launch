from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from www.models import LoanReq
from www.forms import LoanReqForm
from datetime import datetime

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        form = LoanReqForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            aLoan = LoanReq(amount=cd['amount'],
              purpose=cd['purpose'],
              req_date=datetime.now())
            aLoan.save()
            return HttpResponseRedirect('www/home.html')
    else:
        form = LoanReqForm()
    return render(request, 'www/index.html', {'form': form})



def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'www/login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('www/home.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/www/login')
#    return render(request, 'www/login.html')
#    return HttpResponseRedirect('www/home.html')
#    return redirect('www/home.html')
