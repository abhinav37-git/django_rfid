from django.urls import path
from .views import *

urlpatterns = [
    path('addrecord', AddRecord.as_view()),
    path('demo', DemoRecord.as_view())
]
