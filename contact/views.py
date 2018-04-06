from django.shortcuts import render
from django.views.generic import DetailView, FormView

# Create your views here.
from contact.forms import MessageForm
from contact.models import Message


class MessageDetailView(DetailView):
    model = Message


class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/succes'