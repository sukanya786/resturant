from django.db import models

# Create your models here.
class ContactForm(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)


    def __str__(self):
        return self.firstname + self.lastname + self.email + self.subject + self.message

class BookingTable(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    tabletype = models.CharField(max_length=20)
    guestnumber = models.CharField(max_length=70)
    placement = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    note = models.CharField(max_length=150)


    def __str__(self):
        return self.firstname + self.lastname + self.email + self.tabletype + self.placement + self.note
    
    def __int__(self):
        return self.guestnumber + self.date + self.time

class BookMeal(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    itemname = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)


    def __str__(self):
        return self.name + self.itemname
    
    def __int__(self):
        return self.number + self.quantity