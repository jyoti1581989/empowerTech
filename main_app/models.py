from django.db import models

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
    default=CATEGORIES [0] [0]
    )
  
  def __str__(self):
    return f"{self.title} ({self.id})"
  
  def __str__(self):
    return f"{self.get_category_display()}"
