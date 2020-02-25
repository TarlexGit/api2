from rest_framework import serializers
from cars.models import Car

from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#create user
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email', 'name', 'password', )

#create user
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email', 'groups']

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('user','id', 'color', 'brand', 'car_type', 'vin')

class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car.objects.create(**validated_data)



class CarUpdate(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault(many=True, queryset=Car.objects.all()))
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    # car = CarDetailSerializer()
    class Meta:
        model = Car
        fields = ('id', 'color', 'brand', 'car_type', 'vin')
    def update(self, instance, validated_data):

        instance.vin = validated_data.get('vin', instance.vin)
        instance.car_type = validated_data.get('car_type', instance.car_type)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.color = validated_data.get('color', instance.color)
        instance.save()

        return instance

# class CarDelete(serializers.ModelSerializer):
#     model = Car
#     success_url = reverse_lazy('authors')




# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         max_length=100,
#         style={'placeholder': 'Email', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     remember_me = serializers.BooleanField()