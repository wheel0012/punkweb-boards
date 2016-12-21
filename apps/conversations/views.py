from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Conversation, Message



class ConversationCreate(CreateView):
    model = Conversation
    fields = ['users', 'subject']
    template_name_suffix = '_create_form'


class ConversationUpdate(UpdateView):
    model = Conversation
    fields = ['users', 'subject']
    template_name_suffix = '_update_form'


class ConversationDelete(DeleteView):
    model = Conversation
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('home')


class MessageCreate(CreateView):
    model = Message
    fields = ['content']
    template_name_suffix = '_create_form'


class MessageUpdate(UpdateView):
    model = Message
    fields = ['content']
    template_name_suffix = '_update_form'


class MessageDelete(DeleteView):
    model = Message
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('home')
