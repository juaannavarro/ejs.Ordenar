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