from django.db import models


class LoanReq(models.Model):
    req_amount_ini = models.PositiveIntegerField(default=5)
    req_purpose = models.CharField(max_length=200, default="None")
    req_date = models.DateTimeField()
