from django.contrib import admin


from .models import LoanReq


class LoanReqAdmin(admin.ModelAdmin):
    fields = ['req_amount_ini', 'req_purpose', 'req_date']
    list_display = ['req_amount_ini', 'req_purpose', 'req_date']


admin.site.register(LoanReq, LoanReqAdmin)
