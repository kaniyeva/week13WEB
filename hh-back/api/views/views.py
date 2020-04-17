from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
import json
from api.serializers import CompanySerializer, VacancySerializer, CompanySerializer2

# Create your views here.
# CRUD - Company Model
# Get list of companies - GET
# Create new company - POST
@csrf_exempt
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer=CompanySerializer2(companies, many = True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        request_body=json.loads(request.body)
        serializer=CompanySerializer2(data = request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'error' : serializer.errors})


# Get selected company - GET
# Update selected company - PUT
# Delete a company - DELETE
@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id = id)
        if request.method == "GET":
            serializer = CompanySerializer2(company)
            return JsonResponse(serializer.data)
        elif request.method == "PUT":
            request_body=json.loads(request.body)
            serializer = CompanySerializer2(instance = company, data = request_body)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse({'error' : serializer.errors})

        elif request.method == "DELETE":
            company.delete()
            return JsonResponse({'deleted':True})
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'there is no such company '})

@csrf_exempt
def vacancy_by_company(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
        vacancy = Vacancy(company = company)
        """1company attribute of model"""
        if request.method == "GET":
            vacancies = Vacancy.objects.filter(company = company_id)
            serializer=VacancySerializer(vacancies, many = True)
            return JsonResponse(serializer.data, safe = False)
        elif request.method == 'POST':
            request_body = json.loads(request.body)
            serializer=VacancySerializer(vacancy,data=request_body)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse({'error' : serializer.errors})
    except:
        return JsonResponse({'error': 'No vacancies in the company'})

@csrf_exempt
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer=VacancySerializer(vacancies, many = True)
        return JsonResponse(serializer.data, safe = False)


@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id = id)
        if request.method == "GET":
           serializer = VacancySerializer(vacancy)
           return JsonResponse(serializer.data)
        elif request.method == "PUT":
           request_body=json.loads(request.body)
           serializer = VacancySerializer(instance = vacancy, data = request_body)
           if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, safe=False)
           return JsonResponse({'error' : serializer.errors})
        elif request.method == "DELETE":
           vacancy.delete()
           return JsonResponse({'deleted':True})
    except:
        return JsonResponse({'error': 'No vacancies with this id'})


@csrf_exempt
def top_ten(request):
    if request.method == "GET":
        vacancy_list_ten = Vacancy.objects.all().order_by('-salary')[:10]
        serializer = VacancySerializer(vacancy_list_ten,many = True)
        return JsonResponse(serializer.data, safe = False)
