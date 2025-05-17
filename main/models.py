from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Rim(models.Model):
    CHOICES = [
        ["Available", "available"],
        ["Finished", "finished"],
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="rims")
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=CHOICES, default="available")
    finished_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Rim added on {self.added_on}: {self.status}"
    

class Print(models.Model):
    rim = models.ForeignKey(Rim, on_delete=models.CASCADE, related_name="prints")
    qnty = models.IntegerField(blank=True, null=True)
    amount = models.BigIntegerField()

    def __str__(self):
        return f"Print, amount: {self.amount}"