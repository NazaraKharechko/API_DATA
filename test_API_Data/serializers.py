from rest_framework import serializers
from .models import API_Data


class Api_Data_Serializer(serializers.ModelSerializer):

    class Meta:
        model = API_Data
        fields = '__all__'
