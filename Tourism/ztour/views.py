from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Header, Post, Gallery
from tinymce.models import HTMLField
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # forms
        contact_form = ContactForm()
        all_header = Header.objects.all()

        # Posts

        all_posts = Post.objects.filter(promote=True)

        context = {
            'all_header': all_header,
            'contact_form': contact_form,
            'all_posts': all_posts,
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            # email = str(form.getValue('email'))
            context = {'email': contact_form.cleaned_data.get('email'),
                       'name': contact_form.cleaned_data.get('name'),
                       'message': contact_form.cleaned_data.get('message'),
                       'contact_number': contact_form.cleaned_data.get('contact_number'),
                       }

            # Send mail function
            send_mail('subject', context['message'] + "  " + context['name'] + " " + context['contact_number'] + " " + context['email'],
                      'drukdial@gmail.com', ['rinchug@gmail.com'])

            return render(request, 'message_submitted.html', context)

        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


class ContactView(View):
    def get(self, request, *args, **kwargs):

        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # email = str(form.getValue('email'))
            context = {'email': contact_form.cleaned_data.get('email'),
                       'name': contact_form.cleaned_data.get('name'),
                       'message': contact_form.cleaned_data.get('message'),
                       'contact_number': contact_form.cleaned_data.get('contact_number'),
                       }

            # Send mail function
            send_mail('subject', context['message'] + "  " + context['name'] + " " + context['contact_number'] + " " + context['email'],
                      'info@mg.tributetoursandtreks.com', ['drukdial@gmail.com'])

            return render(request, 'message_submitted.html', context)
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


class PackageDetailView(DetailView):
    model = Post
    template_name = 'packagedetail.html'

    def get_context_data(self, **kwargs):
        context = super(PackageDetailView, self).get_context_data(**kwargs)
        # forms
        contact_form = ContactForm()
        all_header = Header.objects.filter(activate=True)
        context['all_header'] = all_header
        context['contact_form'] = contact_form

        return context

    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            # email = str(form.getValue('email'))
            context = {'email': contact_form.cleaned_data.get('email'),
                       'name': contact_form.cleaned_data.get('name'),
                       'message': contact_form.cleaned_data.get('message'),
                       'contact_number': contact_form.cleaned_data.get('contact_number'),
                       }

            # Send mail function
            send_mail('subject', context['message'] + "  " + context['name'] + " " + context['contact_number'] + " " + context['email'],
                      'info@mg.tributetoursandtreks.com', ['drukdial@gmail.com'])

            return render(request, 'message_submitted.html', context)
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


class GalleryView(View):
    def get(self, request, *args, **kwargs):
        # forms
        contact_form = ContactForm()
        all_header = Header.objects.all()
        all_gallery_pics = Gallery.objects.all()

        # Posts

        all_posts = Post.objects.all()

        context = {
            'all_header': all_header,
            'contact_form': contact_form,
            'all_posts': all_posts,
            'all_gallery_pics': all_gallery_pics,
        }
        return render(request, "gallery.html", context)

    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            #email = str(form.getValue('email'))
            context = {'email': contact_form.cleaned_data.get('email'),
                       'name': contact_form.cleaned_data.get('name')}

            return render(request, 'message_submitted.html', context)

        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


class ListPackageView(View):
    def get(self, request, *args, **kwargs):
        # forms
        contact_form = ContactForm()
        all_header = Header.objects.all()

        # Posts

        all_posts = Post.objects.all()

        context = {
            'all_header': all_header,
            'contact_form': contact_form,
            'all_posts': all_posts,
        }
        return render(request, "listpackage.html", context)

    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            # email = str(form.getValue('email'))
            context = {'email': contact_form.cleaned_data.get('email'),
                       'name': contact_form.cleaned_data.get('name'),
                       'message': contact_form.cleaned_data.get('message'),
                       'contact_number': contact_form.cleaned_data.get('contact_number'),
                       }

            # Send mail function
            send_mail('subject', context['message'] + "  " + context['name'] + " " + context['contact_number'] + " " + context['email'],
                      'info@mg.tributetoursandtreks.com', ['drukdial@gmail.com'])

            return render(request, 'message_submitted.html', context)

        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


class BookView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, 'book/book.html', context)


class MessagesubmittedView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, 'message_submitted.html', context)
