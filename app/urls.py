from django.conf.urls import url
from app import views



app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'about/$', views.about, name='about'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'SquadZ/$', views.SquadZ, name='SquadZ'),
]