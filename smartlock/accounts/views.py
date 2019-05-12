from django.shortcuts import render, redirect
from accounts.forms.forms import UserSignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import RPi.GPIO as GPIO
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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)

    GPIO.output(7, False)
    GPIO.output(37, True)
    time.sleep(2)
    GPIO.cleanup()
    return redirect('unlocked')


def lock(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)

    GPIO.output(37, False)
    GPIO.output(7, True)
    time.sleep(2)
    GPIO.cleanup()
    return redirect(' locked')
