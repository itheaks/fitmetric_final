from django.shortcuts import render , redirect
from django.views.generic import View
from .models import AppointmentBook
from django.contrib import messages
import validate_email

class AppointmentView(View):
    def get(self,request):
        return render(request,'meets/index.html')
    
    def post(self,request):
        data = request.POST
        if not validate_email.validate_email(data['email']):
            messages.error(request,'Please enter a valid email')
            return render(request,'meets/index.html')
        if len(data['mobile_no_full']) < 10:
            messages.error(request,'Please enter a valid phone number')
            return render(request,'meets/index.html')
        if len(data['name']) < 3:
            messages.error(request,'Please enter a valid name')
            return render(request,'meets/index.html')
        name = data['name']
        date = data['date']
        disease = data['d_name']
        email = data['email']
        phone = data['mobile_no_full']
        AppointmentBook.objects.create(name=name,date=date,email=email,phone=phone,disease=disease)
        messages.success(request,'Appointment Booked Successfully')
        return redirect('appointment_list')
    
def appointment_list(request):
    appointments = AppointmentBook.objects.all()
    return render(request,'meets/appointment_list.html',{'appointments':appointments})


def VideoCallView(request):
    return render(request,'meets/video_call.html')