from django.db import models
from django.urls import reverse
from datetime import date

CATEGORIES = (
  ('E', 'Education'),
  ('N', 'Networking'),
  ('H', 'Highlights')

)

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  category = models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES [0][0]
    )

  def __str__(self):
    return f"{self.get_category_display()}"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'post_id': self.id})

  def comment_for_today(self):
    return self.comment_set.filter(date=date.today()).count() >= len()

class Comment(models.Model):
  description = models.CharField(max_length=100)
  date = models.DateField('Comment Date')

  post = models.ForeignKey(
    Post, 
    on_delete=models.CASCADE
    )

  class Meta:
    ordering = ['-date']