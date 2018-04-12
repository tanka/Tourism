from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, TourEditForm
from django.contrib.auth.models import Group
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Profile, Tour, Guest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.bio = form.cleaned_data.get('bio')
            group = Group.objects.get(name='guestusers')
            user.groups.add(group)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # user Profile creation
            # profile = user.profile.all()

            # context = {'profile': profile, 'user': user}
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profileDashboard(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("USER Does Not Exist")

    return render(request, 'userhandler/index.html', {'user': user})

def profileDetails(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("USER Does Not Exist")

    return render(request, 'userhandler/userdetails.html', {'user': user})

def tourList(request):
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        raise Http404("USER Does Not Exist")

    return render(request, 'userhandler/tourlist.html', {'user': user})

class TourUpdate(UpdateView):
    model = Tour
    success_url = reverse_lazy('tourList')
    fields = ['dateOfArrival', 'duration']
    template_name = 'userhandler/touredit.html'


def editTour(request, user_id):
    if request.method == 'POST':
        tourToSave = get_object_or_404(Tour, pk=((User(pk=request.user.id).tour_set.all()[0]).id))
        form = TourEditForm(request.POST)
        # form.id = tourToSave.id;
        # form.bookedBy = tourToSave.bookedBy
        # form.tourName = tourToSave.tourName
        # form.noOfPeople = tourToSave.noOfPeople
        if form.is_valid():
            tour = form.save()
            # tour.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.profile.country = form.cleaned_data.get('country')
            # user.profile.bio = form.cleaned_data.get('bio')
            # group = Group.objects.get(name='guestusers')
            # user.groups.add(group)
            # user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            # user Profile creation
            # profile = user.profile.all()

            # context = {'profile': profile, 'user': user}
            return redirect('/userhandler/tourlist/request.user.id'+ User.objects.get(pk=user_id))
    else:
    #     instance = get_object_or_404(MyModel, id=id)
    # form = MyForm(request.POST or None, instance=instance)
        tourToEdit = get_object_or_404(Tour, pk=((User.objects.get(pk=user_id)).tour_set.all()[0]).id)
        form = TourEditForm(request.POST or None, instance=tourToEdit)
    return render(request, 'userhandler/touredit.html', {'form': form})
