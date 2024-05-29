from django.shortcuts import render
from .models import Department , Doctor ,Service







def index_view(request):
    departments = Department.objects.all()
    services = Service.objects.all()
    doctors = Doctor.objects.all()
    context = {'departments': departments, 'doctors': doctors , "services":services} 
    return render(request, 'index.html', context)




def department_detail(request, department_id):
    department = Department.objects.get(pk=department_id)
    return render(request, 'blogs.html', {'department': department})



def ml(request):

    return render(request,"ml.html")





