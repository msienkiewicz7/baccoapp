from django.db import models
from django.utils import timezone


def small_directory_path(instance, filename):
    return 'static/images/ingredients/small/' + instance.name.lower() + '_small.' + filename.split(".")[1]

def large_directory_path(instance, filename):
    return 'static/images/ingredients/large/' + instance.name.lower() + '_large.' + filename.split(".")[1]

# Create your models here.
class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank = True)

    TYPE_CHOICES = [
        ('BREAD', 'Bread'),
        ('BASE', 'Base'),
        ('CHEESE', 'Cheese'),
        ('VEGETABLE', 'Vegetable'),
        ('CONDIMENT', 'Contiment'),
        ('EXTRAS', 'Extras'),
    ]

    type = models.CharField(
        max_length = 50,
        choices = TYPE_CHOICES,
    )

    calories = models.IntegerField(default = 0)

    is_vegetarian = models.BooleanField()
    is_vegan = models.BooleanField()

    img_small = models.FileField(upload_to=small_directory_path, blank = True, verbose_name='Small image')
    img_large = models.FileField(upload_to=large_directory_path, blank = True, verbose_name='Large image')

    price = models.DecimalField(max_digits=3, decimal_places=2, default=0) # max 9,99

    def __str__(self):
        return self.name
        # return '[' + self.type + '] ' + self.name






class Sandwich(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)
    # pub_date = models.DateTimeField('date created')
    pub_date = models.DateTimeField(default=timezone.now(), blank=True)


    price = models.DecimalField(max_digits=4, decimal_places=2, default=0) # max 99,99

    def __str__(self):
        return self.name
