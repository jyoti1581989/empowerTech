from django.db import models



# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  category = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.title} ({self.id})'
