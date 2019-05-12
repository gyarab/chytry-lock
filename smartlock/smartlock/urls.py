from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts.forms.forms import UserLoginForm
from django.contrib.auth.views import LoginView
from accounts import views as acc_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login',
        kwargs={"authentication_form": UserLoginForm}), 
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', acc_views.signup, name='signup'),

    url(r'^lock/$', acc_views.lock, name='script-lock'),#lock script
    url(r'^unlock/$', acc_views.unlock, name='script-unlock'),#unlock script

    url(r'^locked/$', TemplateView.as_view(template_name='home_locked.html'), name='locked'),
    url(r'^unlocked/$', TemplateView.as_view(template_name='home_unlocked.html'), name='unlocked'),
    
    url(r'^output', acc_views.unlock, name='script'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

