from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import Group


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
