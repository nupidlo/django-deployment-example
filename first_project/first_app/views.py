from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import AccessRecord, Topic, Webpage, UserProfileInfo
from . import forms

#Create your views here.
def index(request):
    insertions = {
        'insert_me': "Hello. I'm from views.py"
    }
    return render(request, "first_app/index.html", context=insertions)


def gallery(request):
    insertions = {
        'insert_me': "SO NICE XD"
    }
    return render(request, "first_app/gallery.html", context=insertions)


def acc_recs(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': webpages_list
    }
    return render(request, "first_app/acc_recs.html", context=date_dict)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # do smth
            print("VALIDATION SUCCESS")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', { 'form': form })


def ind(request):
    context_dict = {
        'text': 'hello world',
        'number': 100
    }
    return render(request, "first_app/ind.html", context=context_dict)


def other(request):
    return render(request, "first_app/other.html")


def relative(request):
    return render(request, "first_app/rel_url_templ.html")


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(
        request, "first_app/registration.html",
        context={
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        }
    )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to log in and failed!")
            print("Username: {}, password: {}").format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, "first_app/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")
