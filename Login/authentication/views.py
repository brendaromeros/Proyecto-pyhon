from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home (request):
    return render(request, 'authentication/index.html')

def signup (request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request, "Su cuenta ha sido creada satisfactoriamente")
            return redirect('signin')
    except:
        messages.success(request, "Error intente de nuevo")
        return redirect ('home')

        
    return render(request, 'authentication/signup.html')

def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Se ha iniciado sesión satisfactoriamente.")
            fname = user.first_name
            lname = user.last_name
            username = user.username


            return render(request, "authentication/index.html", {'fname':fname, 'lname':lname, 'username':username})
        
        else:
            messages.error(request, "Datos erróneos. Intente de Nuevo")
            return redirect('home')
    return render(request, 'authentication/signin.html')

def signout (request):
    logout(request)
    return redirect('home')

