from django.db import models

# Create your models here.
class Texts(models.Model):
    text1 = models.CharField(max_length = 500)
    text2 = models.CharField(max_length = 500)
    # similarity_score = models.FloatField(null=True, blank=True)

    # def __str__(self):
    #     return f"{self.text1} - {self.text2}"