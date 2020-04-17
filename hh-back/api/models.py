from django.db import models

# Create your models here.
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    name = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    city = models.CharField(max_length=200)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }
    def __str__(self):
        return '{}:{}'.format(self.id, self.name)

class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = 'vacancies'

    name = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    salary = models.FloatField(default=0.0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }
    def __str__(self):
        return '{}:{}'.format(self.id,self.name)