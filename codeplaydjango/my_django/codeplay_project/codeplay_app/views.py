from django.shortcuts import render, redirect
from .forms import PendaftaranForm, SignInForm
from .models import Pendaftaran
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from argon2 import PasswordHasher
from django.urls import reverse



def index(request):
    return render(request, 'codeplay_app/index.html')

def kids(request):
    return render(request, 'codeplay_app/kids.html')

def teen(request):
    return render(request, 'codeplay_app/teen.html')

def about(request):
    return render(request, 'codeplay_app/about.html')


# ph = PasswordHasher()

def pendaftaran(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
        if form.is_valid():
           
            pendaftaran = form.save(commit=False)
            
           
            # hashed_password = ph.hash(form.cleaned_data['password'])
            # pendaftaran.password = hashed_password
            
           
            pendaftaran.save()
            
            return redirect('signin')  
    else:
        form = PendaftaranForm()
    
    return render(request, 'codeplay_app/pendaftaran.html', {'form': form})

# def pendaftaran (request):
#     registered = False

#     if request.method == 'POST':
#         form = PendaftaranForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()

#             return redirect('signin')
#             registered = True
#         else:
#             print(form.errors)
#     else:
#         form = PendaftaranForm()

#     formdict = {'form':form, 'registered':registered}
#     return render(request, 'codeplay_app/pendaftaran.html', formdict)



def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Gunakan email sebagai username untuk autentikasi
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)  # Login pengguna ke session
                return redirect('index')  # Arahkan ke halaman index setelah login berhasil
            else:
                messages.error(request, 'Email atau password salah.')
    else:
        form = SignInForm()

    return render(request, 'codeplay_app/signin.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             user = authenticate(username=email, password=password)

#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Akun tidak ada.")
#     else:
#         form = SignInForm()

#     return render(request, 'codeplay_app/signin.html', {'form': form})
    
@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
