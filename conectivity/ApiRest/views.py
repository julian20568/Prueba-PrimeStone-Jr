#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from ApiRest.models import People
from ApiRest.serializers import PeopleSerializers
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def MetPeople(request):
    if request.method == 'GET':
        Per = People.objects.all()
        #print (Per)
        serializer = PeopleSerializers(Per,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        serializer = PeopleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def people_detail(request,key):
    try:
        Per = People.objects.get(pk=key)
    except People.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeopleSerializers(Per)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeopleSerializers(Per, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Per.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# def conversion():
#     pulgadas = float(input("Ingrese el número de pulgadas: "))

#     metros = 0.0254 * pulgadas
#     print ("La longitud es de ", metros, " metros")

# conversion()

#Número primo
@api_view(['GET'])
def getPrimeNumer(lista, n):
    lista = int(input('¿Hasta qué número quieres la lista?: '))
    cont = 0
    for i in range(2, lista + 1):
        primos = True
        for j in range(2,11):
            if i == j:
                break
            elif i%j == 0:
                primos = False
            else:
                continue
        if primos == True:
            print(' ',i, end='')
            cont += 1
    print('\nHay %u números primos.' % cont )
