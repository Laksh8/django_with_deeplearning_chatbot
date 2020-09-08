from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ChatView

urlpatterns = [
    path("",ChatView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)