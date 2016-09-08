from django import forms

class LoanReqForm(forms.Form):
    req_amount_ini = forms.IntegerField()
    req_purpose = forms.CharField()
