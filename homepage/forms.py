from django import forms
from django.contrib.admin import widgets
from homepage.models import Message

class SentMessage(forms.ModelForm):
    """A form to store the messages sent by visitors"""
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))    
    message = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Message 
        fields = ('name', 'email', 'subject', 'message',)