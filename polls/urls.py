from django.urls import path
from django.conf.urls import url
from polls import views
urlpatterns = [
    url(r'^api/question/(?P<id>[0-9]$)', views.api_question),
    url(r'^api/choice/(?P<id>[0-9]$)', views.choice),
]
