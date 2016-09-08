from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import LoanReq


class LoanReqAdmin(admin.ModelAdmin):
    fields = ['amount', 'purpose', 'date']
    list_display = ['amount', 'purpose', 'req_date']


admin.site.register(LoanReq, LoanReqAdmin)
admin.site.register(Session)