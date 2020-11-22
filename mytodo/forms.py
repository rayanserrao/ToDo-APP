from django import forms

class ToDoform(forms.Form):
    todo_text=forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Add your ToDo' }))

