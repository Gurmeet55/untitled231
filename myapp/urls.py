from django.conf.urls import url

from.import views
urlpatterns=[url(r'^$', views.register ,name='index1'),
             url('login',views.login ,name='index'),
url('thanks', views.template_thanks ,name='index1'),
url('emp', views.employee ,name='index1')
             ]