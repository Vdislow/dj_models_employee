from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        year = 2022 - self.birth_date.year
        return year

    def __str__(self):
        return self.name


class Employee(AbstractPerson):
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    work_experience = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'added model position - {self.position} '
              f'added model salary - {self.salary} '
              f'added model work_experience - {self.work_experience}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.position}'


class Passport(models.Model):
    inn = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    employee_pas = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self):
        inn = self.inn
        if inn[0] == '2':
            return 'Male'
        if inn[0] == '1':
            return 'Female'

    def save(self, *args, **kwargs):
        print(f'added model inn - {self.inn} '
              f'added model id_card - {self.id_card} ')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_card


class WorkProject(models.Model):
    project_name = models.CharField(max_length=100)
    employee_pr = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        print(f'added model project_name - {self.project_name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'added model date_joined - {self.date_joined}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.date_joined


class Client(AbstractPerson):
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        print(f'added model address - {self.address} '
              f'added model phone_number - {self.phone_number}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.address


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'added model vip_status_start - {self.vip_status_start} '
              f'added model donation_amount - {self.donation_amount}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.vip_status_start} - {self.donation_amount}'
