from django.urls import path
from ApiRest import views
from ApiRest import viewsprimenumber

urlpatterns=[
    path('people',views.MetPeople),
    path('people/<int:key>',views.people_detail), #Eliminar y consultar por id
    path('number/<int:num>',viewsprimenumber.getPrimeNumer),

    ###########numeros primos#################
    #path('number/')
]