from django.db import models



class Theme(models.Model):
    mavzu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
