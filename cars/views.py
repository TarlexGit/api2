from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    # authentications_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )
    permission_classes = (IsAuthenticated, )

class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsAdminUser)
    permission_classes = (IsAuthenticated, )

class CarDetailView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    authentications_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
