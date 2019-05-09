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
    url(r'^accounts/', include('django.contrib.auth.urls')), #include the auth app
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login',
        kwargs={"authentication_form": UserLoginForm}), #login page
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'), #home page
    url(r'^signup/$', acc_views.signup, name='signup'), #signup page
    url(r'^output-lock', acc_views.lock, name='script-lock'),#lock script
    url(r'^output-unlock', acc_views.unlock, name='script-unlock'),#unlock script
    url(r'^locked', TemplateView.as_view(template_name='home_locked.html'), name='locked'),
    url(r'^unlocked', TemplateView.as_view(template_name='home_unlocked.html'), name='unlocked'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
