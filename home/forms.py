from django.forms import ModelForm
import .models import ContactForm, BookingTable, BookMeal

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=('firstname', 'lastname', 'email', 'subject', 'message' )

class BookingTable(ModelForm):
    class Meta:
        model=Booktable
        fields=('firstname', 'lastname', 'email', 'tabletype', 'guestnumber', 'placements', 'date', 'time', 'note'  )

class BookMeal(ModelForm):
    class Meta:
        model=Bookmeal
        fields=('name', 'number', 'itemname', 'quantity' )