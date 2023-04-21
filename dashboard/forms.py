from django.forms import ModelForm,DateInput,Form,CharField
from . models import *


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']


class DateInput(DateInput):
    input_type = 'date'
    
class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        widgets = {"due":DateInput()}
        fields = [
            "subject",
            'title',
            'description',
            'due',
            'is_finished'
        ]


class DashboardForm(Form):
    text = CharField(max_length=100,label = "Enter you search :")


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']
