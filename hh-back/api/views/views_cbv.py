from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_object(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    def put(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.data})

    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()

        return Response({'deleted': True})


class Vacancy_by_companyAPIView(APIView):
    def get_company(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def get_vacancy(self,id):
        return Vacancy(company = self.get_company(id))
    def get(self,request,id):
        vacancies = Vacancy.objects.filter(company=self.get_company(id))
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    def post(self,request,id):
        serializer = VacancySerializer(self.get_vacancy(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)



class VacancyDetailsAPIView(APIView):
    def get_object(self, vacancy_id):
        try:
            return Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors })

    def delete(self, request, vacancy_id):
        company = self.get_object(vacancy_id)
        company.delete()

        return Response({'deleted':True})


class TopTenVacanciesAPIView(APIView):
    def get(self, request):
        top_ten = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_ten, many=True)
        return Response(serializer.data)