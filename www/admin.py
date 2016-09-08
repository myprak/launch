from django.contrib import admin


from .models import LoanReq


class LoanReqAdmin(admin.ModelAdmin):
    fields = ['amount', 'purpose', 'date']
    list_display = ['amount', 'purpose', 'req_date']


admin.site.register(LoanReq, LoanReqAdmin)
