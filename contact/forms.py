from django import forms
from contact.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')



class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=250)
    email = forms.EmailField(label='Your email', )
    message = forms.CharField(label='Your Message', widget=forms.Textarea)