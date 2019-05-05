from django.conf.urls import url
from accounts import views as acc_views
#from . import views

urlpatterns=[
	url(r'^signup/$', acc_views.signup, name='signup'),
]
