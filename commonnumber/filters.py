import django_filters
from django import forms

from django_filters import DateFilter

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class MyDateFromToRangeFilter(django_filters.widgets.RangeWidget):
    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(MyDateFromToRangeFilter, self).__init__(attrs)
        if from_attrs:
            self.widgets[0].attrs.update(from_attrs),

        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)
      
    

class NumberFilter(django_filters.FilterSet):
    date_between = django_filters.DateFromToRangeFilter(
    field_name='date', 
    label='',
    widget=MyDateFromToRangeFilter(
    from_attrs={'placeholder':'From', 'class': 'datepicker, myform-control '},
    to_attrs={'placeholder':'To', 'class':'datepicker, myform-control'})
    )
    

    class Meta:
        model = TeerResult
        fields  = '__all__'
        
        
        widgets = {
            'date_between': MyDateFromToRangeFilter(),
            }
        exclude = [
            'commonnumber',
            'firstresult',
            'secondresult',
            'date',
        ]
        
        
