from django.db import models
# Import the User
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.name}"

# Add new Feeding model below Cat model
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100,null=True)
  email = models.CharField(max_length=100,null=True)
  profile_pic = ImageField(blank=True, manual_crop="")

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.name}"
