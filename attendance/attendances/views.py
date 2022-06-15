from django.shortcuts import redirect, render
from .models import Attendance
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


# check in view function (login_required)
@login_required(login_url='login')
def check_in(request):
    attendance = Attendance.objects.filter(user=request.user).last()
    if request.POST:
        if attendance and attendance.status == "check_in":
            messages.error(request, 'You have already checked in')
            return redirect('home')
        else:
            attendances = Attendance()
            attendances.user = request.user
            attendances.check_in = timezone.now()
            attendances.status = 'check_in'
            attendances.save()

            return redirect('check_out')
    return render(request, 'attendances/check_in.html')


# check out view function (login_required)
@login_required(login_url='login')
def check_out(request):
    attendance = Attendance.objects.filter(user=request.user).last()
    if request.POST:
        if attendance and attendance.check_in and attendance.status == "check_in":
            attendance.check_out = timezone.now()
            attendance.duration = attendance.check_out - attendance.check_in
            attendance.status = 'check_out'
            attendance.save()
            print(attendance.check_out - attendance.check_in)
            return redirect('home')
        else:
            messages.error(request, 'You have to check in first')
            return redirect('check_in')

    return render(request, 'attendances/check_out.html')


# dashboard view function (login_required)
@login_required(login_url='login')
def dashboard(request):
    attendances = Attendance.objects.filter(user=request.user)
    return render(request, 'attendances/dashboard.html', {'attendances': attendances})
