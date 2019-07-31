from django.conf.urls import url
from . import views
urlpatterns = [
url("^$",views.home,name="home"),
url(r"^home/$",views.home,name="home"),
url(r"^endpoint/id/(?P<id>[0-9]+)$",views.endpoint,name="endpoint"),
url(r"ajax/$",views.ajax,name="ajax"),
url(r"ajax1/(?P<pid>[0-9]+)/$",views.ajax1,name="ajax1"),
url(r"notification/(?P<id>[0-9]+)/$",views.notification_detail,name="notification_detail"),
url(r"sensor_detail/(?P<id>[0-9]+)/$",views.sensor_detail,name="sensor_detail"),
url(r"clear_notification/(?P<id>][0-9]+)",views.clear_notification,name="clear_notification"),
]
