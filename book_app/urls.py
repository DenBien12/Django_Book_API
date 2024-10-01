from django.urls import path
from . import views
from django.conf import settings 
from .views import BookListView, BookDetailView

urlpatterns = [
    path('api', BookListView.as_view()),
    path('api/<int:pk>', BookDetailView.as_view())
]