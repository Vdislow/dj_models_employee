from employee.models import *
from datetime import date


e1 = Employee.objects.create(position='manager', salary=1234, work_experience=5, name='Vlad', birth_date='1996-11-05')
e2 = Employee.objects.create(position='cat', salary=1222, work_experience=4, name='Boris', birth_date='2018-04-06')
e3 = Employee.objects.create(position='butcher', salary=1224, work_experience=10, name='Billy', birth_date='1972-06-07')
e4 = Employee.objects.create(position='gid', salary=1123, work_experience=4, name='Daria', birth_date='1998-09-27')

p1 = Passport.objects.create(inn='2322321412431', id_card='ID1022442', employee_pas=e1)
p2 = Passport.objects.create(inn='2498451951918', id_card='ID6151985', employee_pas=e2)
p3 = Passport.objects.create(inn='2651621989798', id_card='ID6198981', employee_pas=e3)
p4 = Passport.objects.create(inn='1598498495223', id_card='ID2199879', employee_pas=e4)

del1 = Employee.objects.latest('id')
del1.delete()

wp = WorkProject.objects.create(project_name='Shawarma House')
wp.employee_pr.set([e1, e2, e3], through_defaults={'date_joined': '2022-08-20'})

wp.employee_pr.remove(e2)


e5 = Employee.objects.create(position='cook', salary=1323, work_experience=6, name='Jimmy', birth_date='1991-04-14')
mem = Membership.objects.create(employee=e5, workproject=wp, date_joined='2022-08-21')


c1 = Client.objects.create(address='Frunze st. 234', phone_number='0222 555 555', name='Oleg', birth_date='2001-03-22')
c2 = Client.objects.create(address='Moscow st. 223', phone_number='7742 2255 555', name='Sophia', birth_date='1994-05-17')
c3 = Client.objects.create(address='Watermelon st. 98', phone_number='225 5558 885', name='Alphia', birth_date='1988-07-07')

vip = VIPClient.objects.create(address='Black st. 414',
                               phone_number='2 544 1447 22',
                               name='James',
                               birth_date='1989-06-07',
                               vip_status_start=date.today(),
                               donation_amount=4568)

c2.delete()



# ЗАПИСИ НИЖЕ ПОЧЕМУ-ТО НЕ ВЫВОДЯТСЯ ЧЕРЕЗ manage.py shell < shell_commands.py
# НО ПРОСТО В shell РАБОТАЮТ



# список всех Employee
emp = Employee.objects.all()

for n in emp:
    print(n.name)


# список всех Employee с паспортными данными
emp_pass = Passport.objects.raw("SELECT id, (SELECT name FROM employee_employee WHERE employee_passport.employee_pas_id = employee_employee.id) FROM employee_passport")

for na in emp_pass:
    print(na.name)


# все проекты
work = WorkProject.objects.all()

for w in work:
    print(w.project_name)


# проекты в которых трудитесь "Вы"
work_wm = Membership.objects.raw("SELECT id,(SELECT project_name FROM employee_workproject WHERE employee_workproject.id = employee_membership.workproject_id) FROM employee_membership WHERE (SELECT name FROM employee_employee WHERE employee_employee.id = employee_membership.employee_id) = 'Vlad'")

for w in work_wm:
    print(w.project_name)


# все Клиенты
clients = Client.objects.all()

for c in clients:
    print(c.name)


# Все ВИП Клиенты
vipall = VIPClient.objects.raw('SELECT *,(SELECT name FROM employee_client WHERE employee_client.id = employee_vipclient.client_ptr_id) FROM employee_vipclient')

for v in vipall:
    print(v.name)
