from django.urls import path
from ApiRest import views

urlpatterns=[
    path('people',views.MetPeople),
    path('people/<int:key>',views.people_detail)

    ###########numeros primos#################
    #path('number/')
]