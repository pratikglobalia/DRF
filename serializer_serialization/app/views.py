from django.shortcuts import render
from .models import Student
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Model object - single student data
def student_detail(request, pk):
    # stu = Student.objects.get(id=2)
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data)


# All model object
def student_data(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data, safe=False)
