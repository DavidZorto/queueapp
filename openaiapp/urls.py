from django.urls import path
from .views import OpenAIRequestView, LongTaskView

urlpatterns = [
    path('request-openai/', OpenAIRequestView.as_view(), name='request_openai'),
    path('long-task/', LongTaskView.as_view(), name='long_task'), 
]
