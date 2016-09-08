from django import forms

class LoanReqForm(forms.Form):
    amount = forms.IntegerField(label='babs amount', max_value=20, min_value=5)
    purpose = forms.CharField(label='Your label', max_length=100)
