from django.urls import path
from .views import (
    ArticleListView, RegisterView, ArticleDetailView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
