"""smartlock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts.forms.forms import UserLoginForm, UserSignUpForm
from django.contrib.auth.views import LoginView
from accounts import views as acc_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('accounts.urls')), #accounts app, must be above the auth app
    url(r'^accounts/', include('django.contrib.auth.urls')), #include the auth app
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login', kwargs={"authentication_form": UserLoginForm}),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'), #home page
    url(r'^signup/$', acc_views.signup, name='signup'),
    url(r'^output', acc_views.unlock, name='script'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

