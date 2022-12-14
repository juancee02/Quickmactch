
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

from juego.models import *
import random
from random import shuffle
from juego.forms import *
import MySQLdb

from django.views.generic import ListView, DetailView 
from django.http import HttpResponse
import string
from .forms import SelectForm
 


# Create your views here.

#creacion de la pagina de incio 
def inicio (request):
    #cart = Cartas.objects.all()#Hacemos  la consulta en base de daros para mostrar las cartas en la vista de iniio 
    #context = { #diccionario de datos para pasar datos dinamicos en el template 
    #    'cart':cart,
    #}
    return render (request, 'inicio.html') #retornamos la vista 

#formulario de registro de usuarios para el juego 

def register (request):
    if request.method == 'POST': #utilizamos el metodo de envio de datos d
        form = UserCreationForm(data = request.POST)#validamos el formulario de para registrarse 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']#donde requerimos los datos que vamos a enviar 
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password) #para que el usuario se authentifique
            login(request, user) #para que el usuario # si todas estas funciones se cumplen el usuario ya se puede logear 
            return redirect('inicio')
    
    else:
        form = UserCreationForm()

    context ={
        'form':form,
    }

    return render(request, 'register.html', context)
"""
def juegos(request):
    barajar = Cartas.objects.all()

    
    context = {
        'barajar':barajar,
    }
    
    return render(request, 'juegos/iniciar_juego.html', context,)

def todas_las_cartas(request):
    detalle = Cartas.objects.all()
    

    context = {
        'detalle':detalle,
        
    }

    return render (request, 'Cart.html' ,context)

            

"""
def barajar (request):
    
    db=MySQLdb.connect(host="localhost",user="root",passwd="",db="quickmatch", )
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM juego_cartas ORDER BY RAND() LIMIT 8;")
    result_set = c.fetchall()
    
   
    #cartas = baraja.objects.all()
    
  
    baraja = [result_set]


    random.shuffle(baraja)
    #jugador1 =print(baraja)
    
    c.execute("SELECT * FROM juego_cartas ORDER BY RAND() LIMIT 8;")
    result_seti = c.fetchall()
    baraja1 = [result_seti]
    jugador2 = []
    random.shuffle(baraja1)
    #jugador2 =print(baraja1)

    
    
   
    imagenes = result_set
    baraja1 = result_seti
    



    context = {
        
        
        
       
        'imagenes':imagenes, 
        'baraja1': result_seti
          
          
        }

    return render(request,'juegos/partida.html',context)


def generate_random(request):
    context = {}

    if request.method == 'POST': # 1
        form = SelectForm(request.GET) # 2
        if form.is_valid(): # 3
            choice = form.cleaned_data['select_choice'] # 4 
            if choice == 'short': # 5
                number = ...
            elif choice == 'normal':
                ...
            else:
                ...

            context.update({'number': number}) # 6
    else:
        context.update({'form': SelectForm()}) # 7

    return render(request, "index.html", context)





def Partida(request):
    return render (request,'juegos/partida.html')

def sala(request):
    return render (request,'juegos/sala.html')







