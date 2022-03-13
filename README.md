Hemos resuelto los ejercicios de ordenar y para ello hemos utilixado la siguiente dirección de github:
https://github.com/juaannavarro/ejs.Ordenar


# Ejercicio 1:

```

 
t = [15,68,75,34,2,35,56] 
inicio=0
fin=len(t)

class ordenacion_dicotomica:

  def __init__(self,tabla,inicio,fin):
    self.t=t
    self.inicio=inicio
    self.fin=fin
    
  def ordenar(self):
    while self.inicio < self.fin:
      for i in range (self.inicio+1,self.fin):
 ```
      
      
      
 # Ejercicio 2:
 
 ```
 
 import random
lista_tareas = []

def crear_tareas():
  if len(lista_tareas) < 10:
    i = random.randint(1,10)
    j = random.randint(1,10)
    if i >= j:
      crear_tareas()
    else:
      tarea = f"{i,j}"
      lista_tareas.append(tarea)
      crear_tareas()
  else:
    return lista_tareas
crear_tareas()
print({lista_tareas})

def ordenar_tareas():
  lista_tareas.sort()
  print({lista_tareas})
ordenar_tareas()

tareas =["Sacar la basura" ,"Fregar", "Poner la lavadora", "Hacer la comida", "Limpiar los baños","Aspirar", "Tender la ropa","Poner la mesa", "Sacar el lavavajillas"]
diccionario = {}

def nombrar_tareas():
  if len(tareas) != 0 or len(lista_tareas) != 0:
    numero_random = random.randint(0,len(tareas) - 1)
    tarea_escrita=tareas.pop(numero_random)
    tarea_numero = lista_tareas.pop(0)
    diccionario[tarea_escrita] = tarea_numero
    nombrar_tareas()
  else:
    
    print(f"{diccionario}\n")
    lista_tareas_ordenada=diccionario.keys()
    print("Las tareas son en orden de prioridad:" , {lista_tareas_ordenada})
nombrar_tareas()

```

# Ejercicio 3:

```

import random

lista_numero= []
print("¿Cuál es el tamaño que quieres para la lista?")
tamaño_lista=int(input())
print("Establece un intervalo inferior")
inf=int(input())
print("Establece un intervalo superior")
sup=int(input())

def crear_lista():
  if len(lista_numero) < tamaño_lista:
    numero=random.randint(inf,sup)
    lista_numero.append(numero)
    crear_lista()
  else:
    return lista_numero
crear_lista()

def ordenarlista_dicotomia(lista_numero):
  for i in range(len(lista_numero)):
    for j in range(i, len(lista_numero)):
      if lista_numero[i] > lista_numero[j]:
        lista_numero[i], lista_numero[j] = lista_numero[j], lista_numero[i]
  print("La lista ordenada con una sola tabla es es la siguiente: ",  {lista_numero})
ordenarlista_dicotomia(lista_numero)
    
lista1= []
lista2 = []
listafinal = []
cota_sup=len(lista_numero)
numero_medio=(cota_sup)// 2

def dicotomia(numero_medio):
  if numero_medio > 0:
    lista1.append(lista_numero.pop(numero_medio))
    dicotomia(numero_medio-1)
  if numero_medio == 0 and len(lista_numero) > 0:
    lista2.append(lista_numero.pop(numero_medio))
    dicotomia(numero_medio)
dicotomia(numero_medio)

listafinal=listafinal+ lista1 + lista2
print("La lista final con dicotomía es:",  {listafinal})

```
