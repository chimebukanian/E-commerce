from django.db import models
from django.conf import settings

# Create your models here.
CATEGORIES=(
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABELS=(
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)
class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.CharField(choices=CATEGORIES, default='S', max_length=2)
    label=models.CharField(choices=LABELS, default='P', max_length=2)

    def __str__(self):
        return self.title


class Orderitem(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(Orderitem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
