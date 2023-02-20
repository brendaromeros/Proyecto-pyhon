from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
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
            fname = user.first_name
            lname = user.last_name
            username = user.username


            return render(request, "authentication/menu.html", {'fname':fname, 'lname':lname, 'username':username})
        
        else:
            messages.error(request, "Datos erróneos. Intente de Nuevo")
            return redirect('home')
    return render(request, 'authentication/signin.html')

def signout (request):
    logout(request)
    return redirect('home')

def relatos (request):
    return render(request, 'viñetas/relatos.html')

def liricas (request):
    return render(request, 'viñetas/liricas.html')

def escritos (request):
    return render(request, 'viñetas/escritos.html')

def principal (request):
    return render(request, 'authentication/menu.html')

def index (request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'app/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'app/upload.html')