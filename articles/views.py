from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article
# Create your views here.


class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = "articles_list"
    login_url = 'login'

    # def get_queryset(self):
    #     query_set = Article.objects.filter(author=self.request.user)
    #     return query_set


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name: str = 'article_detail.html'
    context_object_name = 'article'
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'body']
    login_url = 'login'
    # To get login user and passed to author field

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs):  # new
    #     obj = get_user(request.user)
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')
    login_url = 'login'
