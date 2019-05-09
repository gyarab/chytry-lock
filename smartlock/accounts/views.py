from django.shortcuts import render, redirect
from accounts.forms.forms import UserSignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# import RPi.GPIO as GPIO
import time


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})


def unlock(request):
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(37, GPIO.OUT)

    # GPIO.output(37, True)
    time.sleep(10.5)
    # GPIO.cleanup()
    return HttpResponseRedirect(reverse('unlocked'), request)


def lock(request):
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(37, GPIO.OUT)

    # GPIO.output(37, True)
    time.sleep(10.5)
    # GPIO.cleanup()
    return redirect('/locked')
