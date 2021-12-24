from django.db import models

# Create your models here.
class WFMTTaskModel(models.Model):
    cp_number=models.CharField(max_length=100)
    sne_id=models.IntegerField()
    scheme_number=models.IntegerField()
    trs=models.CharField(max_length=10)
    estimate=models.CharField(max_length=100)

    def __str__(self):
        return self.cp_number
        