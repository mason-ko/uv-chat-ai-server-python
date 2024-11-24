# translator/urls.py
from django.urls import path
from .views import TranslateMessageView

urlpatterns = [
    path('translate', TranslateMessageView.as_view(), name='translate_message'),
]
