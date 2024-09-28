from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

def home(request):
    return render(request, 'home.html')

def form_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_page')
    else:
        form = StudentForm()
    return render(request, 'form_page.html', {'form': form})

def display_page(request):
    students = Student.objects.all()
    return render(request, 'display_page.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # Get the student or 404
    if request.method == 'POST':
        student.delete()  # Delete the student
        return redirect('display_page')  # Redirect to the display page
    return render(request, 'delete_student.html', {'student': student})

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)