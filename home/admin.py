from django.contrib import admin
from .models import ContactForm, BookingTable, BookMeal
# Register your models here.
admin.site.register(ContactForm)
admin.site.register(BookingTable)
admin.site.register(BookMeal)