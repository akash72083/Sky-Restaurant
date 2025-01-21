from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Iten_name = models.CharField(max_length=50)
    description = models.TextField()
    Price = models.IntegerField()
    Category =models.ForeignKey(ItemList, related_name = 'Name', on_delete = models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Iten_name

class AboutUs(models.Model):
    Description = models.TextField()

class Feedback(models.Model):
    User_name = models.CharField(max_length=50)
    Description = models.TextField()
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='Items/',blank=True)

    def __str__(self):
        return self.User_name
    
class BOOK_TABLE(models.Model):
    Name = models.CharField(max_length=122)
    Number = models.IntegerField()
    Email = models.EmailField()
    Person = models.IntegerField()
    Date = models.DateField()

    def __str__(self):
        return self.Name