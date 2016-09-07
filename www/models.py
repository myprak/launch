from django.db import models


class LoanReq(models.Model):
    req_amount_ini = models.PositiveIntegerField(default=0)
    req_date = models.DateTimeField()
