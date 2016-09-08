from django.db import models


class LoanReq(models.Model):
    amount = models.PositiveIntegerField(default=5)
    purpose = models.CharField(max_length=200, default="None")
    req_date = models.DateTimeField()
