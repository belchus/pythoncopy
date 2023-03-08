from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import *
from .models import *

def saludo(req):
 return HttpResponse("Hola coder")

def probando(req):
 mi_html = open('C:/Users/belu9/Desktop/EntregaPython/ProyectoCoder/AppCoder/static/index.html')
 plantilla = Template(mi_html.read())
 mi_html.close()
 contexto = Context()
 documento = plantilla.render(contexto)
 return HttpResponse(documento)
 
def Login(request):
    return render(request,'login.html')

def Register(req):
    return render(req,'register.html')

def inicio(request):
    return render(request, 'index.html')

def Contacto(request):
    return render(request, 'contacto.html')

def Movies(request):
    return render(request, 'movie.html')

def Lista(request):
    return render(request, 'lista.html')

def Reviews(request):
    return render(request, 'perfil.html')

def Busqueda(request):
    return render(request, 'busqueda.html')

def Resultados(request):
    return render(request, 'resultados.html')


def Resultados2(request):
    return render(request, 'resultados-or.html')

#Formulario para agregar un producto a nuestra base de datos
def add_form(request):
    if request.method == "POST":
        addmovie = AddMovie(request.POST)

        if addmovie .is_valid():
            data = addmovie.cleaned_data
            newProd = Movie(
                title=data['title'],
                img=data['img'],
                            
                description=data['description'],
                tag=data['tag']
                            )

            newProd.save()
            return redirect(inicio)
            


        else:
            return render(request, 'movies.html', {'AddMovie': AddMovie})
    
    addmovie= AddMovie()
    return render(request, 'movies.html', {'AddMovie': AddMovie})



#Formulario para agregar una orden  a nuestra base de datos

def review_form(request):
    if request.method == "POST":
        addreview = AddReview(request.POST)

        if addreview .is_valid():
            data = addreview.cleaned_data
            newRev = Review(title=data['title'],
                            img=data['img'],
                            user=data['user'],
                            date=data['date'],
                            stars=data['stars'],
                            text =data['text'])

            newRev.save()
            return redirect(inicio)
        else:
            return render(request, 'perfil.html', {'AddReview': AddReview})    

    addreview = AddReview()
    return render(request, 'perfil.html', {'AddReview': AddReview})

#Formulario para agregar una tienda a nuestra base de datos

def fav_form(request):
    if request.method == "POST":
        myFavs = AddFav(request.POST)

        if myFavs.is_valid():
            data = myFavs.cleaned_data
            newFav = Movie(name=data['name'],
                             address=data['address'],
                             phone=data['phone'],
                              online=data['online'])

            newFav.save()
            return redirect(inicio)

    myFavs = AddFav()
    return render(request, 'lista.html', {'AddFav': AddFav})

#Formulario para buscar un producto en nuestra base de datos    

def find_movie(request):

    if request.GET['title']:
        title = request.GET['title']
        movies = Movie.objects.filter(title__icontains=title)

        return render(request, 'resultados.html', {'movies': movies, 'title': title})

    else:
        respuesta = "No se ha encontrado la pelicula deseada"

    return HttpResponse(respuesta)
    
#Formulario para buscar una orden de pedido en nuestra base de datos 

def find_order(req):

    if req.GET['number']:
        number = req.GET['number']
        orders = Order.objects.filter(number__icontains=number)

        return render(req, 'resultados-or.html', {'orders': orders, 'number':number})

    else:
        respuesta = "El numero de orden buscada no existe"

    return HttpResponse(respuesta)

def login_request(req):
    form = UserCreationForm()

    if req.method == 'POST':
        form = UserCreationForm(req, data = req.POST)

        if form.is_valid():
            user = form.cleaned_data.get('user')
            passw = form.cleaned_data.get('pass')

            user = authenticate(user = user, passw = passw)

            if user is not None:
                login(req, user)
                return render(req, 'login-suc.html', {'message': f'Welcome, {user}!'})

            else:
                return render(req, 'login.html', {'message': f'Error: el usaurio no existe', 'form': form})
        else:
            return render(req, 'login.html', {'message':f'Error, datos incorrectos', 'form':form})
    context = {'form': form}
    return render(req, 'login.html', context)


def register(req):
    if req.method == 'POST':

        form = UserCreationForm(req.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            form.save()
            return render(req, 'success.html', {'message': "Usuario creado"})

    else: 
        form = UserCreationForm()

    return render(req, 'register.html', {'form': form})


