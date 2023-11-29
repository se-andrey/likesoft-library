from django.urls import path
from .views import BookCreateListView, BookDataView


urlpatterns = [
    path('books/', BookCreateListView.as_view(), name='book-list-create'),
    path('books/<int:pk>', BookDataView.as_view(), name='book-detail'),
]
