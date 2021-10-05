from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser


#Número primo

def getPrimeNumer(request, num):

    cont = 0
    for i in range(2, num + 1):
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
    print("Prueba commit")
    #print('\nHay %u números primos.' % cont )
    return HttpResponse("primos {num}")