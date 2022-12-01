from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticlesListView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit')
]
