from braces import views
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article
# Create your views here.


class ArticlesListView(views.LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = "articles_list"
    redirect_field_name = 'hollback'
    raise_exception = False
    login_url = 'login'


class ArticleDetailView(views.LoginRequiredMixin, DetailView):
    model = Article
    template_name: str = 'article_detail.html'
    context_object_name = 'article'
    login_url = 'login'


class ArticleCreateView(views.LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'body']
    login_url = 'login'
    # To get login user and passed to author field

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(views.LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']
    login_url = 'login'


class ArticleDeleteView(views.LoginRequiredMixin, views.PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')
    login_url = 'login'
    permission_required = 'article_delete'
