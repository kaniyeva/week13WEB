from rest_framework import generics
from rest_framework import mixins
from api.models import Vacancy, Company
from api.serializers import VacancySerializer, CompanySerializer2
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    #permission_classes = (IsAuthenticated,)
    """
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs) """
class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_url_kwarg = 'vacancy_id'


    #permission_classes = (IsAuthenticated,)
"""
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs) """

class TopTenAPIView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class Vacancy_by_companyAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_url_kwarg = 'company_id'



class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    permission_classes = (IsAuthenticated,)



class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    lookup_url_kwarg = 'id'
