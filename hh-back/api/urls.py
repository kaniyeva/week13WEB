from django.urls import path,include

from api.views import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView, TopTenAPIView
#from hh_back.api.views.views_cbv import VacanciesByCompanyIdAPIView
#from api.views.views_cbv import Vacancy_by_companyAPIView
from api.views import vacancy_by_company
from . import views
from api.views.views_cbv import *
from api.views import views
from api.views.views_generic import *
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    path('', CompanyListAPIView.as_view()),

    # path('api/companies/', views.company_list),
    # path('api/companies/<int:company_id>/', views.company_detail),
    # path('api/companies/<int:company_id>/vacancies/', views.vacancies_by_companyId),
    #
    # path('api/vacancies', views.vacancy_list),
    # path('api/vacancies/<int:vacancy_id>/', views.vacancy_detail),
    # path('api/vacancies/top_ten/', views.top_ten_vacancies)

    # FBV
    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_detail),
    # path('companies/<int:company_id>/vacancies/', vacancy_by_companyId),
    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vacancy_id>', vacancy_detail),
    # path('vacancies/top_ten', top_ten_vacancies)
    #Authentication
    path('login/', obtain_jwt_token),

    # CBV
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopTenAPIView.as_view())

]