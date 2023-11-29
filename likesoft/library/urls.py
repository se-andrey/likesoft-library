from django.urls import path
from .views import BookCreateListView, BookDataView


urlpatterns = [
    path('book/', BookCreateListView.as_view(), name='book-list-create'),
    path('book/<int:pk>', BookDataView.as_view(), name='book-detail'),
]
