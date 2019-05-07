from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts.forms.forms import AuthForm, SignUpForm
from django.contrib.auth.views import LoginView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')), #accounts app, must be above the auth app
    url(r'^accounts/', include('django.contrib.auth.urls')), #include the auth app
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login', kwargs={"authentication_form": AuthForm}),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'), #home page
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

