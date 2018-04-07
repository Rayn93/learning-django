from django.shortcuts import render
from django.views.generic import DetailView, FormView

# Create your views here.
from contact.forms import MessageForm, ContactForm
from contact.models import Message


class MessageDetailView(DetailView):
    model = Message


class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()
    #     return super(MessageAddView, self).form_valid(form)




