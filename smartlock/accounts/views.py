from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from accounts.forms.forms import UserSignUpForm
#import RPi.GPIO as GPIO
import time

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=user_password)
            user.save()
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})
    
    
def unlock(request):
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(37, GPIO.OUT)

    #GPIO.output(37, True)
    time.sleep(10.5)	
    #GPIO.cleanup()
    return render(request, 'home.html')

