from functools import reduce
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Franchise, Player, Stadium
from .forms import PlayerForm, StadiumForm, UserRegisterForm, ProfileForm

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the IPL App!')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        
        print(username, email, password, confirmPassword)
        return HttpResponse('User registered successfully')
    else:
        return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return HttpResponse('User logged in successfully')
    else:
        return render(request, 'login.html')

def register_franchise(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        short_name = request.POST.get('short_name')
        founded_year = request.POST.get('founded_year')
        no_of_trophies = request.POST.get('no_of_trophies')
        city = request.POST.get('city')
        owner = request.POST.get('owner')
        coach = request.POST.get('coach')
        logo = request.FILES.get('logo')

        Franchise.objects.create(
            name=name,
            short_name=short_name,
            founded_year=founded_year,
            no_of_trophies=no_of_trophies,
            city=city,
            owner=owner,
            coach=coach,
            logo=logo
        )
        return HttpResponse('Franchise registered successfully')
    else:
        return render(request, 'register_franchise.html')

def franchise_list(request):
    franchises = Franchise.objects.all()
    return render(request, 'franchise_list.html', { 'franchises': franchises })

def franchise_details(request, id):
    franchise = Franchise.objects.get(id=id)
    return render(request, 'franchise_details.html', { 'franchise': franchise })

def update_franchise(request, id):
    franchise = Franchise.objects.get(id=id)
    if request.method == 'POST':
        franchise.name = request.POST.get('name')
        franchise.short_name = request.POST.get('short_name')
        franchise.founded_year = request.POST.get('founded_year')
        franchise.no_of_trophies = request.POST.get('no_of_trophies')
        franchise.city = request.POST.get('city')
        franchise.owner = request.POST.get('owner')
        franchise.coach = request.POST.get('coach')
        
        if request.FILES.get('logo'):
            franchise.logo = request.FILES.get('logo')

        franchise.save()
        return redirect('franchise_list')
    else:
        return render(request, 'update_franchise.html', { 'franchise': franchise })

def delete_franchise(request, id):
    franchise = Franchise.objects.get(id=id)

    if request.method == 'POST':
        franchise.delete()
        return redirect('franchise_list')

def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
        else:
            return HttpResponse('Invalid data', status=400)
    else:
        form = PlayerForm()
        return render(request, 'register_player.html', { 'form': form })

def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', { 'players': players })

def register_stadium(request):
    if request.method == 'POST':
        form = StadiumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stadium_list')
        else:
            print(form)
            return HttpResponse('Invalid data', status=400)
    else:
        form = StadiumForm()
        return render(request, 'register_stadium.html', { 'form': form })

def stadium_list(request):
    stadiums = Stadium.objects.all()
    return render(request, 'stadium_list.html', { 'stadiums': stadiums })

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            # Create user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponse('Your account has been created! You can login into your account.')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

        return render(request, 'register_user.html', { 'user_form': user_form, 'profile_form': profile_form })

def login_user(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                # return HttpResponse('You have successfully logged in!')
            else:
                # return HttpResponse('Incorrect username or password')
                messages.error(request, 'Incorrect username or password')
    else:
        login_form = AuthenticationForm()

    return render(request, 'login_user.html', { 'login_form': login_form })