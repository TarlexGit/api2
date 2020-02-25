from rest_framework import generics
from cars.serializers import *
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
#create user
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# Activate User athtr regiser
from django.dispatch import receiver
from django.db.models.signals import pre_save

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import UpdateAPIView
from django.template.response import TemplateResponse, HttpResponse
from rest_framework import renderers
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is False:
        print("Creating active User")
        instance.is_active = True
    else:
        print("Updating User Record")


#create user

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer





class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'cars/newCar.html'
    # def post(self, request):
    #     car = Car.objects.all()
    #     queryset = get_object_or_404(Car)
    #     serializer = CarCreateSerializer(queryset, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'queryset': queryset})
    #     serializer.save()
    #     return redirect('/api/v1/cars/usercars/')


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    authentications_classes = TokenAuthentication
    permission_classes = (IsAuthenticated, )#IsAdminUser
    
class CarDetailView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()  
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

### Home Page ####
from django.shortcuts import render
def cars_index(request, *args, **kwargs):
    return render(request, 'cars/index.html')




class UserListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cars/allCars.html'
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        ### Вызов для авторизированого юзера !!!*
        u = self.request.user
        queryset = Car.objects.filter(user_id = u)
        serializer = CarListSerializer(Car)
        return Response({'serializer': serializer, 'cars': queryset}, template_name='cars/allCars.html',)


from django.core import serializers       
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import action
# def redirect_all_cars(request):
#     return redirect('all_cars', permanent=True)


class CarDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cars/changeCar.html'
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        car = Car.objects.all()
        queryset = get_object_or_404(Car, pk=pk)
        serializer = CarUpdate(queryset)
        response = Response({'serializer': serializer, 'car': queryset})
        return response
        
    def post(self, request, pk):
        car = Car.objects.all()
        queryset = get_object_or_404(Car, pk=pk)
        serializer = CarUpdate(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'queryset': queryset})
        serializer.save()
        return redirect('/api/v1/cars/usercars/')
        
# def car_create(request):
#     return render(request, 'cars/newCar.html')
from rest_framework import mixins
from rest_framework import status
from django.http import Http404
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
class CarCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cars/newCar.html'
    serializer_class = CarCreateSerializer
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        return Response({}, template_name = 'cars/newCar.html')
        
    def post(self, request):
        # car = Car.objects.create(vin=request.POST, car_type=request.POST, color=request.POST, brand=request.POST)
        self.request.POST._mutable = True
        data = request.data
        data['user'] = request.user.id
        serializer = CarCreateSerializer(data=self.request.data, context={'request':request})
        if serializer.is_valid():
            
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return redirect('/api/v1/cars/usercars/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

    