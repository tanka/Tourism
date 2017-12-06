from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm

# Create your views here.


def home(request):

    return render(request, "base.html", {'value': True})


class ContactView(View):
    def get(self, request, *args, **kwargs):

        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            #email = str(form.getValue('email'))
            context = {'email': form.cleaned_data.get('email'),
                       'name': form.cleaned_data.get('name')}

            return render(request, 'message_submitted.html', context)
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})

    # context = {}
    # return render(request, "contact.html", context)


class BirdWatchingView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, 'book/birdwatching.html', context)


class BookView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, 'book/book.html', context)


class MessagesubmittedView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, 'message_submitted.html', context)
