from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=200)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=4000)
    number_of_pages = models.CharField(max_length=100)

    def __str__(self):

        return self.title
