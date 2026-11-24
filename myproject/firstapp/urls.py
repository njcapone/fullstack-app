from django.urls import path
from . import views
# this file maps urls on the application l
# each url path has an address and a the associated view
urlpatterns = [
    path('function', views.hello_world),
    path('class', views.hello_philippines.as_view()),
]

# still need to map URLs to the project level