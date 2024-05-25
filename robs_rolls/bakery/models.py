from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class WeeklyTreat(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    week_start = models.DateField()
    week_end = models.DateField()

    def __str__(self):
        return f"{self.product.name} ({self.week_start} - {self.week_end})"
