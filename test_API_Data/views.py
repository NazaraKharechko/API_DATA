from django.shortcuts import render
from .models import API_Data
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import generics
from .serializers import Api_Data_Serializer


def cramp(request):
    tasks_obj = API_Data.objects.all
    return render(request, 'cramp.html', {"alltasks": tasks_obj})


class CreateVieAll(ListModelMixin, CreateAPIView):
    serializer_class = Api_Data_Serializer
    queryset = API_Data.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FindVieData(ListModelMixin, CreateAPIView):
    serializer_class = Api_Data_Serializer

    def get_queryset(self, ):
        params = self.request.query_params
        date = params.get('date', None)
        if not date:
            return API_Data.objects.all()
        return API_Data.objects.filter(date=date)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
