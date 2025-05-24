from django.db import models

# Create your models here.
class Item(models.Model):
    CHOICES = [
        ('product', 'Product'),
        ('service', 'Service'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CHOICES, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)  # e.g., "pcs", "kg"
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


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


# Order 
class Order(models.Model): 
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    sold_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.item.category == 'product' and self.quantity is None:
            raise ValidationError("Quantity is required for product sales.")
        if self.item.category == 'service' and self.quantity is not None:
            raise ValidationError("Quantity must be empty for service sales.")

    def __str__(self):
        return f"Sale of {self.item.name} on {self.sold_on}"