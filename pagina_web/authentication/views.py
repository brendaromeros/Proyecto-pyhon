from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
"""
Aqu{i se guardan todas las funciones
que se utilizan para qu ela p{agina fucione.
"""


def home(request):
    logout(request)
    return render(request, 'authentication/index.html')


"""
Esta función dirige al home donde abrira el archivo
index.html el cual contiene el registo e inicio de sesión.
"""


def signup(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()
            messages.success(request, "Se ha creado su ceunta.")
            return redirect('signin')
    except Exception:
        messages.success(request, "Error intente de nuevo.")
        return redirect('home')

    return render(request, 'authentication/signup.html')


"""
Esta función se encarga de registrar al usuario
cuya información se registra en una base de datos sqlite3
en la carpeta paginaweb
"""


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            username = user.username

            messages.success(request, "Ha iniciado sesión.")

            return render(request,
                          "authentication/menu.html",
                          {'fname': fname,
                           'lname': lname,
                           'username': username})
        else:
            messages.error(request, "Datos erróneos. Intente de Nuevo.")
            return redirect('home')
    return render(request, 'authentication/signin.html')


"""
Esta función se encarga de iniciar sesión autenticando
que el usuario esté registrado y si este no está en la base
no lo dejará registrarse.

"""


def signout(request):
    logout(request)
    messages.success(request, "Ha cerrado sesión")
    return redirect('home')


"""
Esta función se encarga de salirse de la sesión
y regresar a home con una notificación de que
el proceso ha sido exitoso.
"""


def principal(request):
    return render(request, 'authentication/menu.html')


"""
Esta función se encarga de redirigir al archivo
menu.html
"""


def aportes(request):
    return render(request, 'viñetas/aportes.html')


"""
Esta función se encarga de redirigir al archivo
aportes.html
"""


def escritos(request):
    return render(request, 'viñetas2/escritos.html')


"""
Esta función se encarga de redirigir al archivo
escritos.html
"""


def relatos(request):
    return render(request, 'viñetas4/relatos.html')


"""
Esta función se encarga de redirigir al archivo
relatos.html
"""


def liricas(request):
    return render(request, 'viñetas3/liricas.html')


"""
Esta función se encarga de redirigir al archivo
liricas.html
"""


def profile(request):
    return render(request, 'authentication/profile.html')


"""
Esta función se encarga de redirigir al archivo
profile.html
"""


def comentarios(request):
    return render(request, 'js/comentaries.html')


"""
Esta función se encarga de redirigir al archivo
comentarios.html
"""
