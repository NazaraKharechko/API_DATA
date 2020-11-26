from django.db import models


class API_Data(models.Model):
    class Meta:
        db_table = 'API_Data'

    date = models.DateField()
    client_name = models.CharField(max_length=20)
    provider_name = models.CharField(max_length=20)
    revenue = models.IntegerField()
    wons = models.IntegerField()
    date_updated = models.DateField()
    date_created = models.DateField()

