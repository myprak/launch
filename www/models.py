from django.db import models


class Loan_Desired(models.Model):
    amount = models.PositiveIntegerField(default=0)
    req_date = models.DateTimeField()
